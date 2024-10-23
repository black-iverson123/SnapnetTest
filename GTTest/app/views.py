from flask import Flask, render_template, request, redirect, url_for, session, flash
from app import app, db
from app.forms import LoginForm, Signup, NewBags
from flask_login import login_user, login_required, current_user
from app.models import User, Bags



@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This view handle the user login details and checks if user exist or not before response

    Returns:
        Checks if user exist or not....
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data ).first() or User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
                flash('Bad login credentials!!!', 'danger')
                return redirect(url_for('index'))
                
        login_user(user)
        session['name'] = current_user.username
        session['user_id'] = current_user.id
        return redirect(url_for('dashboard'))
    return render_template('index.html', title='Log In ', form=form)

@app.route('/register', methods=['GET','POST'])
def signUp():
    """This view is responsible for registering new users on the platform, data validation here is handled by flask form

    Returns:
        redirects back to login page
    """
    form = Signup()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        
        return redirect(url_for('index'))
    else:
        return render_template('signup.html', title='Sign Up',  form=form)

@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    This view function displays the data to logged in users after authentication
    Returns:
        _type_: Inventory in database
    """
    bags = Bags.query.all()    
    return render_template('dash.html', title='Dashboard', bags=bags)


@app.route('/shop<int:bag_id>', methods=['GET', 'POST'])
@login_required
def shop(bag_id):
    """_summary_
    This view collects the id of the bag and add to session till check out
    Args:
        bag_id (_type_): this is the integer associated with the bag by default primary key

    """
    session['bag'] == []
    bag = Bags.query.get_or_404(bag_id)
    session['bag'].append({'id': bag.id, 'name': bag.name, 'price': bag.price})
    return redirect(url_for('cart'))


            
@app.route('/add_bag', methods=['GET','POST'])
@login_required
def create_bag():
    """
    View function that opens form to create a new inventory

    Returns:
        user to dashboard after inventory is successfully created, data validation is handled by flaskform
    """
    form = NewBags()
    if form.validate_on_submit():
        # form is valid, proceed with creating the community
        bag = Bags(name=form.name.data, price=form.Price.data)
        db.session.add(bag)
        db.session.commit()
        flash(f'{bag.name} has been added to inventory!!!', 'success')
        return redirect(url_for('dashboard'))
    else:
        return render_template('create_bag.html', form=form)
       


    
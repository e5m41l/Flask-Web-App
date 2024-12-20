from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route("/logout", methods=['GET'])
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            pass
        elif len(firstName) < 2:
            flash('First name must be greater than 3 characters.', category='error')
            pass
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
            pass
        elif len(firstName) < 8:
            flash('Password must be at least 8 characters.', category='error')
            pass
    else:
        flash('Account created!', category='success')
        #add user to the db
        pass
    return render_template("signUp.html")

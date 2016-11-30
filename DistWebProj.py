from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database URL format = databaseType://username:password@endpoint:port/DatabaseName
# note: username and password is taken out for secure purposes. gotta figure out how to do environmental variables.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dlewis:password@distweb.c7b6ayuxu8b8.us-east-2.rds.amazonaws.com:5432/distWebDB'


database = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def add_user():
    login_error = None
    register_error = None
    registered = None
    if request.method == 'POST':
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            if username == "" or username.strip() == "" or password == "" or password.strip() == "":
                login_error = "PLEASE FILL IN ALL THE FIELDS!"
            else:
                from objects import UserAccount
                user = UserAccount.query.filter_by(username=username).first()
                if user == None or user.password != password:
                    login_error = "username or password is incorrect"
                else:
                    return render_template('HomePage.html',username=username)
        elif 'register' in request.form:
            username = request.form['username']
            password = request.form['password']
            if username == "" or username.strip() == "" or password == "" or password.strip() == "":
                register_error = "PLEASE FILL IN ALL THE FILEDS!"
            else:
                from objects import UserAccount
                user = UserAccount.query.filter_by(username=username).first()
                if user != None:
                    register_error = "User already exist!"
                else:
                    user = UserAccount(username,password)
                    database.session.add(user)
                    database.session.commit()
                    registered = "Registered!"
    return render_template('LoginPage.html',login_error=login_error,register_error=register_error,registered=registered)

@app.route('/home')
def home_page():
    return render_template('HomePage.html', db=database)

@app.route('/post_user', methods=['POST'])
def post_user():
    from objects import UserAccount
    userAccount = UserAccount(request.form['username'], request.form['password']) ## grab the data from the form.
    database.session.add(userAccount) # form the SQL to insert.
    database.session.commit() # run the actual sql command.
    return redirect(url_for('add_user')) # rever the user back to the  create user form.

@app.route('/products')
def products_page():
    return render_template('ProductsPage.html')

@app.route('/thankyou')
def thankyou_page():
    return render_template('ThankyouPage.html')

@app.route('/motherboards')
def mobo_page():
    from objects import MotherBoard
    return render_template('productTemplate.html', table=MotherBoard)


@app.route('/RAM')
def ram_page():
    from objects import Ram
    return render_template('productTemplate.html', table=Ram)

@app.route('/CPUs')
def cpu_page():
    from objects import CPU
    return render_template('productTemplate.html', table=CPU)


@app.route('/PSUs')
def psu_page():
    from objects import Powersupply
    return render_template('productTemplate.html', table=Powersupply)

@app.route('/VideoCards')
def gpu_page():
    from objects import GPU, UserAccount
    return render_template('productTemplate.html', table=GPU)


# @app.route('/Coolers')
# def cooler_page():
#     from objects import Cooler
#     return render_template('productTemplate.html', table=Cooler)

@app.route('/HardDrives')
def hardDive_page():
    from objects import HardDrive, UserAccount
    return  render_template('productTemplate.html',table=HardDrive)

# @app.route('/SSDs')
# def ssd_page():
#     from objects import SSD
#     return render_template('productTemplate.html',table=SSD)

# @app.route('/Towers')
# def tower_page():
#     from objects import Tower
#     return render_template('productTemplate.html', table=Tower)

@app.route('/cart')
def cart_page():
    return render_template('CartPage.html')





if __name__ == '__main__':
    app.run(debug=True)

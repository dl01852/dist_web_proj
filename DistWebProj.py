from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import webbrowser


app = Flask(__name__)
# database URL format = databaseType://username:password@endpoint:port/DatabaseName
# note: username and password is taken out for secure purposes. gotta figure out how to do environmental variables.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dlewis:password@distweb.c7b6ayuxu8b8.us-east-2.rds.amazonaws.com:5432/distWebDB'
app.secret_key = "abcdef"
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
                    session['username'] = username
                    return render_template('ProductsPage.html',username=username)
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
                    user = UserAccount(id=None,username=username,password=password)
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
    username = session['username']
    return render_template('ThankyouPage.html',username=username)

@app.route('/motherboards')
def mobo_page():
    from objects import MotherBoard
    username = session['username']
    return render_template('productTemplate.html', table=MotherBoard,username=username)


@app.route('/test')
def test():
    return render_template('productTemplate.html')

@app.route('/RAM')
def ram_page():
    from objects import Ram
    username = session['username']
    return render_template('productTemplate.html', table=Ram,username=username)

@app.route('/CPUs',methods=['GET','POST'])
def cpu_page():
    from objects import CPU, UserAccount,Cart
    username = session['username']
    if request.method == 'POST':
        cpuId = request.form['id']
        username = request.form['username']
        cpu = CPU.query.filter_by(id=cpuId).first()
        user = UserAccount.query.filter_by(username=username).first()
        if user != None:
            cart = Cart.query.filter_by(userid=user.id).first()
            if cart == None: # if cart exist does not, then exist it you and add item to it.
                userCart = Cart(user.id,user.id,None,cpu.id,None,None,None,None)
                database.session.add(userCart)
                database.session.commit()
            elif cart != None:
                cart.cpuid = cpu.id
                database.session.commit()
    return render_template('productTemplate.html', table=CPU,username=username)


@app.route('/PSUs')
def psu_page():
    from objects import Powersupply
    username = session['username']
    return render_template('productTemplate.html', table=Powersupply, username=username)

@app.route('/VideoCards')
def gpu_page():
    from objects import GPU, UserAccount
    username = session['username']
    return render_template('productTemplate.html', table=GPU,username=username)


# @app.route('/Coolers')
# def cooler_page():
#     from objects import Cooler
#     return render_template('productTemplate.html', table=Cooler)

@app.route('/HardDrives')
def hardDrive_page():

    from objects import HardDrive, UserAccount
    username = session['username']
    return  render_template('productTemplate.html',table=HardDrive,username=username)

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
    from objects import UserAccount, Cart
    username = session['username']
    # user = UserAccount.query.filter_by(username=username).first()# get the user.
    # cart = Cart.query.filter_by(userid=user.id).first() # get that users cart.
    # if cart == None: # if no cart.
    #     return render_template('CartPage.html')
    # else:
    #     picPrice =[] # list to hold a picture and price of the part selected.
    #     for part in cart:
    #         if part == None:
    #             continue
    #         picPrice.append((part.img,part.price))

    return render_template('CartPage.html',items=Cart,username=username)



if __name__ == '__main__':
    app.run(debug=True)

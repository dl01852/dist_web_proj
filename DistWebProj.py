from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database URL format = databaseType://username:password@endpoint:port/DatabaseName
# note: username and password is taken out for secure purposes. gotta figure out how to do environmental variables.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dlewis:password@distweb.c7b6ayuxu8b8.us-east-2.rds.amazonaws.com:5432/distWebDB'

database = SQLAlchemy(app)

@app.route('/')
def add_user():
    return render_template('HomePage.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    from objects import User
    userAccount = User(request.form['username'], request.form['password']) ## grab the data from the form.
    database.session.add(userAccount) # form the SQL to insert.
    database.session.commit() # run the actual sql command.
    return redirect(url_for('add_user')) # rever the user back to the  create user form.


@app.route('/products')
def products_page():
    return render_template('ProductsPage.html')

@app.route('/motherboards')
def mobo_page():
    from objects import User
    users = User.query.all()
    return render_template('MotherBoardPage.html', users=users)


@app.route('/RAM')
def ram_page():
    return render_template('RAMPage.html')

@app.route('/CPUs')
def cpu_page():
    return render_template('CPUPage.html')


@app.route('/PSUs', methods=['POST', 'GET'])
def psu_page():
    from objects import Powersupply
    supplies = Powersupply.query.all()
    return render_template('PSUPage.html',supplies=supplies)

@app.route('/VideoCards')
def gpu_page():
  return render_template('GPUPage.html')
#@app.route('/HardDrives')
#def hardDrive_page():
#    return render_template('HardDrivePage.html')

#@app.route('/Cases')
#def cases_page():
#   return render_template('CasesPage.html')

#@app.route('/SSDs')
#def ssds_page():
#   return render_template('SSDPage.html')

#@app.route('/Coolers')
#def cooler_page():
#   return render_template('CoolersPage.html')

#@app.route('/OperatingSystems')
#def os_page():
#   return render_template('OSPage.html')




if __name__ == '__main__':
    app.run(debug=True)


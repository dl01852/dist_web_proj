from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# database URL format = databaseType://username:password@endpoint:port/DatabaseName
# note: username and password is taken out for secure purposes. gotta figure out how to do environmental variables.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{USERNAME}:{PASSWORD}@distweb.c7b6ayuxu8b8.us-east-2.rds.amazonaws.com:5432/{DATABASE NAME}'

database = SQLAlchemy(app)

@app.route('/')
def add_user():
    return render_template('add_user.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    from objects import User
    userAccount = User(request.form['username'], request.form['password'])
    database.session.add(userAccount)
    database.session.commit()
    return redirect(url_for('add_user'))


@app.route('/products')
def products_page():
    return render_template('ProductsPage.html')


if __name__ == '__main__':
    app.run(debug=True)

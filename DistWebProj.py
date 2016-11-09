from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/products')
def products_page():
    return render_template('ProductsPage.html')

if __name__ == '__main__':
    app.run()

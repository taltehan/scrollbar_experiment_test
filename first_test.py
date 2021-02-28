from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<a href="secondPage">Hello, World!</a>'


@app.route('/secondPage')
def second_page(x='hi'):
    return x


if __name__ == '__main__':
    app.run(debug=True)

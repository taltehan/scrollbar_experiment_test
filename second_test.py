from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('hello.html')


@app.route('/secondPage')
def second_page(x='hi'):
    return x


@app.route('/sample')
def sample():
    return render_template('page_sample.html')


if __name__ == '__main__':
    app.run(debug=True)

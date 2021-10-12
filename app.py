from logging import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/<string:name>')
def print_name(name):
    return 'Hi, ' + name


if __name__ == '__main__':
    app.run(debug=True)
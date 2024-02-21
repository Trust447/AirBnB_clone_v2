#!/usr/bin/python3
"""
script that starts a Flask web application 
application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")

@app.route('/', strict_slashes=False)
def display():
    """returns strings"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """displays text and replaces _ with a space"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>")
def py_text(text="is cool"):
    """displays text and replaces _ with a space"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)

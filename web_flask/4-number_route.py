#!/usr/bin/python3
"""a script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def display():
    """returns a string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns a string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb(text):
    """returns a string"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/(<text>)", strict_slashes=False)
def hbnb(text="is cool"):
    """returns a string"""
    return "C {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

import os
from flask import Flask, request


app = Flask(__name__)


app.route("/shorturl")
def shortner():
    print(request.args)
    return f"Hello World"
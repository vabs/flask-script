#token = 9742f1eb4004b6da8b27a655d0729b44178163ca


import json
import traceback
import sys

__author__ = 'vsomani'

from flask import Flask
from flask import render_template, request, jsonify
import requests
import pprint
from github import Github, Label

app = Flask(__name__)
app.debug = True


@app.route('/')
def home_page():
    return jsonify({"status": "ok"})




if __name__ == "__main__":
    app.run()

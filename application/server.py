from application import app
import os
from flask import Flask
import sys

@app.route('/')
def index():
    return(str(sys.version_info[0]) + '.' + str(sys.version_info[1]))


@app.route('/health')
def health():
    return('ok')


@app.route('/hello')
def health():
    return('Hello World')

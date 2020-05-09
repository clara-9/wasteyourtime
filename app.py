# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:14:34 2020

@author: crull
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_name():
    return "hello"

if __name__ == '__main__':
    app.run()
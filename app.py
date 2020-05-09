# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:14:34 2020

@author: crull
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_name():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
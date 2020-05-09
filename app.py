# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:14:34 2020

@author: crull
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_name():
    return render_template("main.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
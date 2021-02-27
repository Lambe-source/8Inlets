import os
from flask import Flask, jsonify, render_template, redirect

application = app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    

import os
from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__, static_folder='./static')
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route for staff login page
@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

# Route for staff portal after login page
@app.route('/staff_portal', methods=['POST'])
def staff_portal():
    return render_template('staff_portal.html')

# Route for new staff account creation
@app.route('/onboarding', methods=['POST'])
def onboard_redirect():
    return render_template('onboarding.html')

# Route for signing out gym members
@app.route('/member_signout', methods=['POST'])
def signout_redirect():
    return render_template('signout_members.html')
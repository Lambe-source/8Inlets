import os
from flask import Flask, jsonify, render_template

application = app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    
# Route for new member page 
@app.route('/new_member', methods=['POST'])
def new_member():
    return render_template('new_member.html')

# Route for returning member page 
@app.route('/returning_member', methods=['POST'])
def returning_member():
    return render_template('returning_member.html')

# Route for staff members 
@app.route('/staff_portal', methods=['POST'])
def staff_portal():
    return render_template('staff_portal.html')

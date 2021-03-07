import os
import boto3
from flask import Flask, jsonify, render_template, redirect, request
from boto3.dynamodb.conditions import Key

application = app = Flask(__name__)
app.secret_key = os.urandom(24)

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

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

# Route to verfity returning member exists in dynamoDB
@app.route('/verify', methods=['POST'])
def verify_user():
    # message use from: https://overiq.com/flask-101/form-handling-in-flask/
    message = ""
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']

        table = dynamodb.Table('Members')
        response = table.query(
            KeyConditionExpression=Key('Name').eq(name) & Key('PhoneNo').eq(phone_number)
        )
        items = response['Items']
        user = items[0]
        if user:
            message = "Log in successful!"
        else:
            message = "User not found!"
    return render_template('returning_member.html', message=message)

# Route for staff members 
@app.route('/staff_portal', methods=['GET'])
def staff_portal():
    #url = "http://www.google.com"
    url = "http://0.0.0.0:5001/"
    return redirect(url)
    #return render_template('staff_portal.html')

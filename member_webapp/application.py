import os
import boto3
from flask import Flask, jsonify, render_template, url_for, redirect, request
from boto3.dynamodb.conditions import Key

application = app = Flask(__name__)
app.secret_key = os.urandom(24)

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    
# Route for new member page 
@app.route('/new_member', methods=['POST', 'GET'])
def new_member():
    return render_template('new_member.html')

# Route for returning member page 
@app.route('/returning_member', methods=['POST'])
def returning_member():
    return render_template('returning_member.html')

# Route to verify returning member exists in dynamoDB
@app.route('/returning_member/log_in', methods=['POST'])
def verify_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_id = int(user_id)

        table = dynamodb.Table('Members')
        response = table.query(
            KeyConditionExpression=Key('Id').eq(user_id)
        )
        items = response['Items']
        if items:
            user = items[0]
            return render_template('check_in.html', login_message="Login successful!", user_id=user['Id'])
        else:
            return render_template('returning_member.html', error="User not found!")

# Route to switch user's attendance status in dynamoDB
@app.route('/returning_member/check_in/<user_id>', methods=['POST'])
def attendance(user_id):
    if request.method == 'POST':
        user_id = int(user_id)
        checked = request.form.get('check-in')
        if checked:
            table = dynamodb.Table('Members')
            response = table.update_item(
                Key={'Id': user_id},
                UpdateExpression="set attendance=:t",
                ExpressionAttributeValues={ ':t': True },
                ReturnValues="UPDATED_NEW"
            )
            return render_template('check_in.html', success="Check in successful!")
        else:
            return render_template('check_in.html', user_id=user_id,
                                check_in_message="Did not check in. Please select the box to indicate your attendance.")

# Route for staff members 
@app.route('/staff_portal', methods=['GET'])
def staff_portal():
    #url = "http://www.google.com"
    url = "http://0.0.0.0:5001/"
    return redirect(url)
    #return render_template('staff_portal.html')

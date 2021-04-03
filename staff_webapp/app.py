import os
import boto3
import uuid
from flask import Flask, jsonify, render_template, redirect, request
from boto3.dynamodb.conditions import Key

app = Flask(__name__, static_folder='./static')
app.secret_key = os.urandom(24)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route for staff login page
@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

# Route for staff portal after login page
@app.route('/staff_portal', methods=['POST','GET'])
def verify_staff_login():
    if request.method == 'POST':
        staff_id = request.form['staff_id']

        table = dynamodb.Table('Staff')
        response = table.query(
            KeyConditionExpression=Key('Id').eq(staff_id)
        )
        items = response['Items']
        if items:
            user = items[0]
            return render_template('staff_portal.html', login_message="Login successful!")
        else:
            return render_template('login.html', error="Staff account not found!")

# Route for new staff account creation
@app.route('/onboarding', methods=['POST'])
def onboard_redirect():

    return render_template('onboarding.html')

# Route for signing out gym members
@app.route('/member_signout', methods=['POST'])
def signout_redirect():
    return render_template('signout_members.html')

@app.route('/get_staff_member_data', methods=['GET', 'POST'])
def get_staff_member_data():
    if request.method == 'POST':
        Name = request.form['Name']
        PhoneNo = request.form['PhoneNo']
        staff_member_id_number = str(uuid.uuid4())
        table = dynamodb.Table('Staff')
        table.put_item( 
                Item={
                    'Id': staff_member_id_number,
                    'Name': Name,
                    'PhoneNo': PhoneNo,
                }
            )
        r = ["Success!", "Your staff ID is: " + staff_member_id_number, "Please keep this on hand."]
        return render_template('onboarding.html', msg=r)
    r= ' '
    return render_template('onboarding.html', msg=r)

# Route to verify member exists in dynamoDB
@app.route('/sign_out', methods=['POST'])
def verify_user():
    if request.method == 'POST':
        user_id = request.form['user_id']

        table = dynamodb.Table('Members')
        response = table.query(
            KeyConditionExpression=Key('Id').eq(user_id)
        )
        items = response['Items']
        if items:
            user = items[0]
            return render_template('uncheck_attendance.html', success_message="ID Found!", 
                user_id=user['Id'], 
                user_name=user['Name'])
        else:
            return render_template('signout_members.html', user_not_found_error="User not found!")

# Route to switch user's attendance status in dynamoDB
@app.route('/sign-out/checkbox/<user_id>', methods=['POST'])
def attendance(user_id):
    if request.method == 'POST':
        checked = request.form.get('sign-out')
        if checked:
            table = dynamodb.Table('Members')
            response = table.update_item(
                Key={'Id': user_id},
                UpdateExpression="set attendance=:t",
                ExpressionAttributeValues={ ':t': 0 },
                ReturnValues="UPDATED_NEW"
            )
            return render_template('uncheck_attendance.html', success="Sign-out successful!")
        else:
            return render_template('uncheck_attendance.html', error="Signout Unsuccessful.")

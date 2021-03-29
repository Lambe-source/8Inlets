import os
import uuid
import boto3
from flask import Flask, jsonify, render_template, redirect, request
from boto3.dynamodb.conditions import Key
import hashlib
import json

application = app = Flask(__name__, static_folder='./static')
app.secret_key = os.urandom(24)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name='us-east-1',
)
get_secret_value_response = client.get_secret_value(
            SecretId="dev/hashing/key1"
)
salt = json.loads(get_secret_value_response.get('SecretString')).get('hash_key')


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
    url = "http://0.0.0.0:5001/"
    return redirect(url)
    
@app.route('/get_member_data', methods=['GET', 'POST'])
def get_member_data():
    if request.method == 'POST':
        Name = request.form['Name']
        PhoneNo = request.form['PhoneNo']
        CreditCard = request.form['CreditCard']
        EmContact = request.form['EmContact']
        member_id_number = str(uuid.uuid4())
        table = dynamodb.Table('Members')
        
        # Encrypt CreditCard Info
        CreditCard = CreditCard + salt
        h = hashlib.md5(CreditCard.encode())

        table.put_item( 
                Item={
            'Id': member_id_number,
            'Name': Name,
            'PhoneNo': PhoneNo,
            'CreditCard': str(h.hexdigest()),
            'EmContact': EmContact,
            'waiver': True,
            'attendance': False
                    }
            )
        r = ["Success!", "Your member ID is:" + member_id_number, "Please keep this on hand."]
        return render_template('new_member.html', msg=r)
    r= ' '
    return render_template('new_member.html', msg=r)

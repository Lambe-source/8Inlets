import os
import uuid
import boto3
from flask import Flask, jsonify, render_template, redirect, request


application = app = Flask(__name__)
app.secret_key = os.urandom(24)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

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
@app.route('/staff_portal', methods=['GET'])
def staff_portal():
    #url = "http://www.google.com"
    url = "http://0.0.0.0:5001/"
    return redirect(url)
    #return render_template('staff_portal.html')

@app.route('/get_member_data', methods=['GET', 'POST'])
def get_member_data():
    if request.method == 'POST':
        Name = request.form['Name']
        PhoneNo = request.form['PhoneNo']
        CreditCard = request.form['CreditCard']
        EmContact = request.form['EmContact']
        member_id_number = str(uuid.uuid4())
        table = dynamodb.Table('Members')
        #member_id_number += table.item_count
        table.put_item( 
                Item={
            'Id': member_id_number,
            'Name': Name,
            'PhoneNo': PhoneNo,
            'CreditCard': CreditCard,
            'EmContact': EmContact,
            'waiver': True,
            'attendance': False
                    }
            )
        r = 'Success! Your member ID is:'+ member_id_number+'\n Please keep this on hand.'
        return render_template('new_member.html', msg=r)
    r= ' '
    return render_template('new_member.html')

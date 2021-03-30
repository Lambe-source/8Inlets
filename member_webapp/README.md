SaaSy Cloud Group 34
Group Project for CSCI 4145

To run app locally: 
`flask run`

If that doesn't work, try: 
`python -m flask run`


DYNAMODB INSTRUCTIONS:

Log into your AWS Educate profile
Once you are in your Vocareum Work Bench click Account Details
A pop up should show with an option to show AWS CLI
Click show and Copy and paste into ~/.aws/credentials
Once that is done go into the AWS workbench
Open up DynamoDB and make a table named 'Members' that just has one key: 'Id' and is a string
Uncheck Use default settings

Click Add Index
* set Primary Key to 'attendance' with type number
* set Index Name as `AttendanceIndex`
* change Projected Attributes to 'Keys only'

In the Auto Scaling section, uncheck both read and write capacity (for testing to not accidentally incur charges).
Once your table and index are made, you are free to use the web app to add new members.

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

#### SECRETS MANAGER INSTRUCTIONS:

* Open up Secrets Manager and click **Store a new secret**
* Set secret type *Other type of secrets*
* For the key/value pair, enter `hash_key` and `7e534649-d7f2-4ff6-a048-998ec810006b`, respectively
* Click next
* Name the secret `dev/hashing/key1` and click next
* Make sure automatic rotation is disabled, if it isn't by default. 
* Click next, review the secret, then click *Store*

####SNS INSTRUCTIONS:

*If you have already set up SNS for the staff app, you can skip it here and begin using the app*

* Open up Simple Notification Service and go to the **Topics** tab. 
* Click *Create topic*
  * Change type to 'Standard'
  * Name it `capacity-notifications`
  * Click *Create topic*
* Once your topic is made, copy the ARN.
  * it will look like `arn:aws:sns:region:account-id:capacity-notifications`
* Store the topic arn in Secrets Manager using the instructions above, but with the following values:
  * The secret type is *Other type of secrets*
  * The secret key is `topic_arn`
  * The secret value is the topic ARN copied above 
  * The secret name is `dev/sns/key1`
  * Automatic rotation is disabled
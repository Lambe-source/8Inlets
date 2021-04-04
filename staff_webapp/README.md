SaaSy Cloud Group 34
Group Project for CSCI 4145

To run app locally: 
`flask run --host=0.0.0.0 --port=5001`

#### DYNAMODB INSTRUCTIONS:

* Log into your AWS Educate profile
    * Once you are in your Vocareum Work Bench, click **Account Details**
* A pop up should show with an option to show AWS CLI
    * Click show and copy and paste into `~/.aws/credentials`
* Once that is done go into the AWS workbench
* Open up DynamoDB and make a table named 'Staff' that just has one key: 'Id' and it is a string
* There must be an existing staff member in order to log in. To create one:
  * Select the **Items** tab and click *Create item*
  * Enter a UUID value as the Id (example: `ee58595f-d1a7-4ace-825a-6cfb586686c2`)
  * Click *Save* and the item with be created.
* Once your table and staff member are made, you are free to use the web app.

#### SNS INSTRUCTIONS:

*If you have already set up SNS for the member app, you can skip it here and begin using the app*

* Open up Simple Notification Service and go to the **Topics** tab. 
* Click *Create topic*
  * Change type to 'Standard'
  * Name it `capacity-notifications`
  * Click *Create topic*
* Once your topic is made, copy the ARN.
  * it will look like `arn:aws:sns:region:account-id:capacity-notifications`
* Store the topic arn in Secrets Manager as follows:
  * Open up Secrets Manager and click **Store a new secret**
  * Set secret type *Other type of secrets*
  * For the key/value pair, enter `topic_arn` and the ARN value copied above, respectively
  * Click next
  * Name the secret `dev/sns/key1` and click next
  * Make sure automatic rotation is disabled, if it isn't by default. 
  * Click next, review the secret, then click *Store*
  
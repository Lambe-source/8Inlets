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

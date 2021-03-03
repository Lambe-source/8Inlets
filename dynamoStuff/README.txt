Right now this is set up for a local instance, via a docker image I pulled off the internet.


IMAGE:
https://hub.docker.com/r/amazon/dynamodb-local
IMAGE PULL COMMAND:
docker pull amazon/dynamodb-local
Ran this via DockerDesktop OR from the command line with:
docker run amazon/dynamodb-local 

Take the json file and run this:
aws dynamodb create-table --cli-input-json file://createTable.json --endpoint-url http://localhost:8000

Check if the table is there:
aws dynamodb list-tables --endpoint-url http://localhost:8000

Then use the put command to enter something into the table

Use scan to see if its there:
aws dynamodb scan --table-name Members  --endpoint-url http://localhost:5000

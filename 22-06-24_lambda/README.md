# Exercise 24/06/22

Exercise to learn the Basics about python fast api and ec2 deployment

### 1. Fetch Job data with a lambda function
1. create a s3 bucket for job data
1. write a lambda python function that fetch the job data from (https://www.arbeitnow.com/api/job-board-api) and creates a json file for every job inside of the s3 bucket
(hint: to use requests you need to upload a source package or a layer with the dependency)

### 2. terraform 
1. create a terraform project that setup the lambda function. (because of the sandbox you can not create the s3 bucket with terraform)

### 3. cloud watch trigger
1. add a cloud watch trigger that calls the lambda function every hour

### 4. CD (optional)
1. Setup a github actions pipeline that deploys your code and infrastructure ( you can use the cli to create the bucket)
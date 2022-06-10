# Exercise 10/06/22

Exercise to learn the Basics about python and apis

We will build da dashboard for corona data

### 1. Setup project
1. create a new git repository 

### 2. create a python script that use the corona api to provide dashboard data 
1. use python to call the [rest api](https://documenter.getpostman.com/view/10808728/SzS8rjbc#27454960-ea1c-4b91-a0b6-0468bb4e6712) to get the latest corona data for germany
1. save a json file that looks like the following.
```
{
    "cases":12345,
    "active": 234,
    "trend": "UP",
    "lockdown": true
}

```
- cases: are all cases
- active: currently infectet
- trend: active cases increases or decreasing over the last 7 days
- lockdown: active over last 7 days over 10.000 

3. Use the python sdk to upload the result `corona-data.json` to an s3 bucket

### 3. terraform (optional)
1. create a terraform project that setup an ec2 instance with python and runs your script every 10 minutes automatically

### 4. CD (optional)
1. Setup a github actions pipeline that deploys your code and infrastructure
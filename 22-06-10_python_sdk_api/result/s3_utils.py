import boto3
s3 = boto3.client('s3')
bucket_name = "some-test123213125dsa"

def upload_to_s3(filename):
    with open(filename, "rb") as f:
        s3.upload_fileobj(f, bucket_name, filename)
import boto3

s3 = boto3.client('s3')
#s3.create_bucket(Bucket='0724amitt')
response = s3.delete_bucket(Bucket= '0724amitt')
print(response)

instance = boto3.client('ec2')

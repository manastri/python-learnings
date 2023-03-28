# To use this script, replace the YOUR_AWS_ACCESS_KEY_ID, YOUR_AWS_SECRET_ACCESS_KEY, YOUR_S3_BUCKET_NAME, and PATH/TO/MONGODB/DUMP placeholders with your own values. Then run the script with Python to restore the latest MongoDB dump to your local database.
import boto3
import subprocess

# Replace with your AWS access key ID and secret access key
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'

# Replace with your S3 bucket name and path to the MongoDB dump
s3_bucket_name = 'YOUR_S3_BUCKET_NAME'
s3_dump_path = 'PATH/TO/MONGODB/DUMP'

# Connect to S3 and find the latest dump file
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
response = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix=s3_dump_path)
latest_dump = max(response['Contents'], key=lambda x: x['LastModified'])

# Download the dump file to a local temporary directory
local_dump_path = '/tmp/latest_dump.tar.gz'
s3.download_file(s3_bucket_name, latest_dump['Key'], local_dump_path)

# Extract the dump file to a temporary directory
subprocess.run(['tar', '-zxvf', local_dump_path, '-C', '/tmp'])

# Restore the MongoDB dump to the local database
subprocess.run(['mongorestore', '/tmp/' + s3_dump_path])

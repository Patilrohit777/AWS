#import boto3
#from botocore.exceptions import NoCredentialsError, PartialCredentialsError
#
#
local_file_path = r'C:\WS\AWS\practice_Scripts\list_iam_users.py'
bucket_name = '4june2023rohitppatil'
s3_file_path = 'list_iam_users.py'

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_file_to_s3(local_file_path, bucket_name, s3_file_path):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file_path, bucket_name, s3_file_path)
        print(f"File '{local_file_path}' uploaded to '{bucket_name}/{s3_file_path}'")
    except FileNotFoundError:
        print(f"The file '{local_file_path}' was not found")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error uploading file: {e}")



upload_file_to_s3(local_file_path, bucket_name, s3_file_path)

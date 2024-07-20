import boto3
from datetime import datetime
import pytz

from datetime import datetime
from dateutil import parser


# Initialize a session using Amazon IAM
client = boto3.client('iam')



def get_access_key_details(access_key_id):
    try:
        response = client.get_access_key_last_used(AccessKeyId=access_key_id)
        return response['AccessKeyLastUsed']
    except ClientError as e:
        print(f"Error retrieving access key details for key {access_key_id}: {e}")
        return None

import boto3
from botocore.exceptions import ClientError

def delete_iam_user(username):
    iam = boto3.client('iam')
    try:
        # Detach all managed policies
        policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        for policy in policies:
            iam.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
        
        # Remove user from all groups
        groups = iam.list_groups_for_user(UserName=username)['Groups']
        for group in groups:
            iam.remove_user_from_group(UserName=username, GroupName=group['GroupName'])

        # Delete access keys
        access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        for key in access_keys:
            iam.delete_access_key(UserName=username, AccessKeyId=key['AccessKeyId'])
        
        # Delete the user
        iam.delete_user(UserName=username)
        print(f"User {username} has been deleted.")

    except ClientError as e:
        print(f"Error: {e}")





def list_all_users():
    # Retrieve the list of IAM users
    print("----------start------------")
    paginator = client.get_paginator('list_users')
    
    for page in paginator.paginate():
        users = page['Users']
        
        # Print the details of each user
        for user in users:
            print(user["UserId"])
            print(user["UserName"])
            user_name = user["UserName"]
            try:
                #response = client.get_login_profile(UserName=user_name)
                response = client.list_access_keys(UserName=user_name)
                access_keys = response['AccessKeyMetadata']
                
                print("access_keys", "======", access_keys)
            except: 
                print("login profile for " + user_name + "not found.")
                
            if access_keys:
                for key in access_keys:
                    access_key_id = key['AccessKeyId']
                    key_details = get_access_key_details(access_key_id)
                    if key_details:
                        last_used = key_details.get('LastUsedDate', 'Never')
                        print(f"  Access Key ID: {access_key_id}, Last Used: {last_used}")
                    else:
                        print(f"  Access Key ID: {access_key_id}, Last Used: No data available")
            else:
                print("  No Access Keys Found")    
            
            
            
               
            
            # Input datetime string
            datetime_str = str(last_used)
            
            # Convert the string to a datetime object
            datetime_obj = parser.isoparse(datetime_str)
            
            # Get the current datetime with timezone info
            current_datetime = datetime.now(datetime_obj.tzinfo)
            
            # Calculate the difference in days
            delta = current_datetime - datetime_obj
            days_between = delta.days
            
            # Print the result
            print("Days between:", days_between)
            
            
            if days_between > 29:
                print("Deleting user with user_name: " + user_name + " as it is older than", days_between,"days" )
                delete_iam_user(user_name)
            
            print("========================================")

            
            
list_all_users()
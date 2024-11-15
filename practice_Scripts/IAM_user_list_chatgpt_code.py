import boto3

#sed -i 'C:\\WS\AWS\\practice_Scripts\\python setup for ec2 instance.txt' filename.py


def list_iam_users_with_ids(region='us-east-1'):
    # Create an IAM client
    iam = boto3.client('iam', region_name=region)
    
    # Initialize the list to store user details
    users_list = []
    
    # List users
    response = iam.list_users()
    users = response.get('Users', [])
    
    for user in users:
        # Retrieve user details including UserId
        user_details = iam.get_user(UserName=user['UserName'])
        user_id = user_details['User']['UserId']
        
        users_list.append({
            'UserName': user['UserName'],
            'UserId': user_id,
            'Arn': user['Arn'],
            'CreateDate': user['CreateDate']
        })
    
    # Print out user details
    for user in users_list:
        print(f"UserName: {user['UserName']}, UserId: {user['UserId']}")

if __name__ == "__main__":
    list_iam_users_with_ids()

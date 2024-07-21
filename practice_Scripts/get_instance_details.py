#####################################################################################
# In this Code we are listing down list of all the instances for particular region.
# We will delete all the instance which has below Values:
# instance_name != None
# ITSO != None
# FSO != None
# building_id != None
#####################################################################################






import boto3



def delete_instance(instance_id, region):
    ec2 = boto3.client('ec2', region_name=region)
    
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} termination initiated successfully.")
    except Exception as e:
        print(f"Error terminating instance {instance_id}: {str(e)}")


def get_ec2_instance_details(region):
    # Create EC2 client with specified region
    ec2 = boto3.client('ec2', region_name=region)

    # Describe EC2 instances
    response = ec2.describe_instances()
    print(response)
    # Extract and print instance details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("===================================================")
            print(instance)
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            public_ip = instance.get('PublicIpAddress')
            private_ip = instance.get('PrivateIpAddress')
            launch_time = instance['LaunchTime']
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

            instance_name = tags.get('instance_name')
            ITSO = tags.get('ITSO')
            FSO = tags.get('FSO')
            building_id = tags.get('Building ID')

            print(f"Instance ID: {instance_id}")
            print(f"Instance Type: {instance_type}")
            print(f"State: {state}")
            print(f"Public IP: {public_ip}")
            print(f"Private IP: {private_ip}")
            print(f"Launch Time: {launch_time}")
            print(f"Instance Name: {instance_name}")
            print(f"ITSO: {ITSO}")
            print(f"FSO: {FSO}")
            print(f"Building ID: {building_id}")
            print('-' * 60)

            if instance_name != None and ITSO != None and FSO != None and building_id !=  None:
                print("All the Parameters have some value assigned so We will Delete It")
                delete_instance(instance_id, region)
            else:
                print("One of the Values is Empty...So Don't Delete It")

if __name__ == "__main__":
    region = 'us-east-1'  # Replace with the desired region
    get_ec2_instance_details(region)

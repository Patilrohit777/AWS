#!/bin/bash

# List all EC2 instance IDs using AWS CLI and store them in a variable
ec2_instances=$(aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId' --output text)

# Check if any EC2 instances were found
if [ -z "$ec2_instances" ]; then
  echo "No EC2 instances found."
  exit 1
fi

# Loop through the EC2 instance IDs and import them into Terraform
for instance_id in $ec2_instances; do
  # Generate a Terraform resource name using the instance ID (replace dashes if necessary)
  resource_name="aws_instance.my_instance"
  
  # Print the instance being imported
  echo "Importing EC2 instance: $resource_name with ID $instance_id"
  
  # Run the terraform import command
  terraform import $resource_name $instance_id
done

echo "All EC2 instances have been imported."

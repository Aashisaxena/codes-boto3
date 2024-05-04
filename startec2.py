import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Define the instance ID to start
instance_id = 'YOUR_INSTANCE_ID_HERE'

# Start the EC2 instance
response = ec2_client.start_instances(InstanceIds=[instance_id])

# Print the start response
print("Starting instance with ID:", instance_id)
print("Response:", response)

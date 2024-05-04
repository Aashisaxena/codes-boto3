import boto3

print("Listing EC2 instances across all regions:")

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Retrieve instances from all regions
response = ec2_client.describe_instances()

# Iterate over reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        # Print instance ID
        print("Instance ID:", instance['InstanceId'])

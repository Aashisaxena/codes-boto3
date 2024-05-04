import boto3

# Initialize the EC2 resource
ec2_resource = boto3.resource('ec2')

# Create a new EC2 instance
instance = ec2_resource.create_instances(
    ImageId='YOUR_AMI_ID_HERE',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)[0]  # Extract the first instance from the returned list

print("New instance created with ID:", instance.id)

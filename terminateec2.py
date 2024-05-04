import boto3

client = boto3.client("ec2")
response = client.describe_instances()

new_list = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        new_list.append(instance['InstanceId'])

print(new_list)

# Terminate the EC2 instance
response = client.terminate_instances(InstanceIds=['i-0854461202d2e5b4d'])

# Print the termination response
print(response)

print("Successfully deleted the instance with instance ID 'i-0854461202d2e5b4d'. Please recheck through AWS Management Console.")

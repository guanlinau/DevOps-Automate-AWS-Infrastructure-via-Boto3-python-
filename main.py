import boto3
import schedule



#Get the vpc info
ec2_client = boto3.client("ec2")

# Method 1: Get the instance state via describe_instances()
# reservations = ec2_client.describe_instances()

# for reservation in reservations['Reservations']:
#     instances = reservation['Instances']
#     for instance in instances:
#         print(f"Instance { instance['InstanceId']}" is {instance['State']['Name']})

# Method 2: Get the instance state with instance staus and system status

def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )

    for status in statuses['InstanceStatuses']:
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        instance_state = status['InstanceState']['Name']
        print(f"The state of instance { status['InstanceId']} is {instance_state} with instance status is {instance_status} and system_status {system_status}")
        print('----------------------\n')

schedule.every(3).minite.do(check_instance_status)

while True:
    schedule.run_pending()
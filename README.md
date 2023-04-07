### Automate AWS Infrastructure via Boto3(python)

### Technologies used:

Terraform, AWS, Docker, Linux, Git, Python, Boto3

### Project Description:

1-Create TF project to automate provisioning AWS Infrastructure and its components, such as: VPC, Subnet, Route Table, Internet Gateway, EC2, Security Group.

2-Configure TF script to automate deploying Docker container to EC2 instance

3- Write a Python script that fetches statuses of EC2 Instances and prints to the console

4- Extend the Python script to continuously check the status of EC2 Instances in a specific interval

### Instruction:

1-Create a terraform.tfvars file under the root of the current folder with the following variables

```
vpc_cidr_block =
subnet_cidr_block =
availability_zone =
env_profix =
my_ip_address =
instance_type =
public_key_location  =
```

2-configure aws credentials with specified region and access_id and secret_key

```
aws configuration
```

3- Initialize the Terraform project

```
terraform init
```

4- Create the VPC and EC2 instance in it

```
terraform apply --auto-approve
```

5- create requirements.txt in the dir folder and add boto3, schedule into requirements.txt
```
pip freeze > requirements.txt
```

6- install boto3
```
pip install -r requirements.txt
```
7- run the main.py 
```
python main.py
```

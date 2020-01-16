import boto3
ec2 = boto3.client('ec2')
response = ec2.create_security_group(GroupName='testgroup2',Description='testme')
ec2.authorize_security_group_ingress(GroupId=response['GroupId'],IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=80,ToPort=80)
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:script',
            'Values': [
                'python',
            ]
        },
    ]
)
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
try:
    response = ec2.create_security_group(GroupName='python',
                                         Description='to be added as required',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 443,
             'ToPort': 443,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '10.0.0.0/24'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)

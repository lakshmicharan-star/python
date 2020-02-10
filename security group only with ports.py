import boto3
import csv
security_group_id = input("security group name : ")
protocol = "tcp"
csv_file = "D:/python/test1.csv"
ec2 = boto3.resource('ec2')
security_group = ec2.SecurityGroup(security_group_id)
f = open(csv_file)
csv_f = csv.reader(f)
for row in csv_f:
    cidr = row[0]
    description = row[1]
    port_range_start = int(row[2])
    port_range_end = int(row[3])
    security_group.authorize_ingress(
        DryRun=False,
        IpPermissions=[
            {
                'FromPort': port_range_start,
                'ToPort': port_range_end,
                'IpProtocol': protocol,
                'IpRanges': [
                    {
                        'CidrIp': cidr,
                        'Description': description
                    },
                ]
            }
        ]
    )
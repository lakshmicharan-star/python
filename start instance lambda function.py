import boto3

ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:env',
            'Values':['test']
        }
    ]
    instances=ec2.instances.filter(Filters=filter)
    for each_in in instances:
        each_in.start()

    return 'Success'
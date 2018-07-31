import boto3
session = boto3.session.Session(region_name= 'us-east-1')
dynamodb = session.resource('dynamodb')


table = dynamodb.Table("TestTable")

filler = "x" * 1000

i = 0
while (i < 10):
    j = 0
    while (j < 10):
        print (i, j)
        
        table.put_item(
            Item={
                'pk':i,
                'sk':j,
                'filler':{"S":filler}
            }
        )
        j += 1
    i += 1



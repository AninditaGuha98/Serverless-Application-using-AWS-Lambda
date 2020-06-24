import json
import mysql.connector
import boto3

conn = mysql.connector.connect(host='serverlessa3.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                               , user='admin',
                               password='serverlessadmin',
                               db='lambda')
cursor = conn.cursor()


def lambda_handler(event, context):
    if event:
        s3 = boto3.client('s3')
        file_object = event["Records"][0]
        file = str(file_object['s3']['object']['key'])
        data = s3.get_object(Bucket='tagsb00845637', Key=file)
        contents = data['Body'].read().decode('utf-8')
        contents = json.loads(contents)
        filename = file.split('.')
        contents_dict = contents[filename[0]]

        for key, value in contents_dict.items():
            find_data = ("select Frequency from frequency where NamedEntity=%s")
            cursor.execute(find_data, (key,))
            results = cursor.fetchone()
            if results:
                final_value = value + results[0]
                update_data = ("update frequency set Frequency=%s where NamedEntity=%s")
                cursor.execute(update_data, (final_value, key))
            else:
                insert_data = ("INSERT into frequency (NamedEntity,Frequency) values(%s,%s)")
                cursor.execute(insert_data, (key, value))

        conn.commit()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




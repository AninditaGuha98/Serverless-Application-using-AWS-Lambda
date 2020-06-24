import json
import nltk
import boto3

nltk.data.path.append('/opt/nltk_data')


def lambda_handler(event, context):
    if event:
        s3 = boto3.client('s3')
        file_object = event["Records"][0]
        file = str(file_object['s3']['object']['key'])
        data = s3.get_object(Bucket='sampledatab00845637', Key=file)
        contents = data['Body'].read().decode('utf-8')

        entity = {}
        word = nltk.word_tokenize(contents)
        word = nltk.pos_tag(word)
        for item in word:
            if item[1] == 'NNP':
                if item[0] in entity:
                    entity[item[0]] += 1
                else:
                    entity[item[0]] = 1
        print(entity)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

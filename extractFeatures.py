author = "Anindita"

import json
import nltk
import boto3

nltk.data.path.append('/opt/nltk_data')


def namedEntity(contents, file):
    entity = {}
    s3File = {}
    word = nltk.word_tokenize(contents)
    word = nltk.pos_tag(word)
    for item in word:
        if item[1] == 'NNP':
            if item[0] in entity:
                entity[item[0]] += 1
            else:
                entity[item[0]] = 1
    print(entity)

    names = file.split('.')
    key = names[0] + 'ne'
    filename = names[0] + 'ne.' + names[1]
    s3File[key] = entity
    uploadJSONtoS3(s3File, filename)


def uploadJSONtoS3(s3File, filename):
    s3 = boto3.resource('s3')
    s3object = s3.Object('tagsb00845637', filename)
    s3object.put(
        Body=(bytes(json.dumps(s3File).encode('UTF-8')))
    )


def lambda_handler(event, context):
    if event:
        s3 = boto3.client('s3')
        file_object = event["Records"][0]
        file = str(file_object['s3']['object']['key'])
        data = s3.get_object(Bucket='sampledatab00845637', Key=file)
        contents = data['Body'].read().decode('utf-8')
        namedEntity(contents, file)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




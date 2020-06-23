author = "Anindita"

import boto3
import glob
import time

# Upload files to S3 bucket
s3 = boto3.client('s3')
for file in glob.glob('tech/*.txt'):
    s3.upload_file(file, "sampledatab00845637", file)
    time.sleep(0.1)

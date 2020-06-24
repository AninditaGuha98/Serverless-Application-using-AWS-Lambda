author = "Anindita"

import boto3
import glob
import time
import re

# Upload files to S3 bucket
s3 = boto3.client('s3')
counter= 1
for file in glob.glob('tech/*.txt'):
    s3.upload_file(file, "sampledatab00845637", str(counter)+'.txt')
    print("upload successful", counter)
    counter=counter+1
    time.sleep(0.1)


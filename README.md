# Serverless-Application-using-AWS-Lambda

<h3> List of tasks: </h3>
<ul>
  <li> Uploaded 400 files from a directory one at a time to the s3 bucket created in the AWS educate account.</li>
  <li> Once a file is added to the bucket, an event must be triggered which calls a function present in AWS lambda. This lambda function converts the text file into named entities. </li>
  <li> The lambda function contains dependencies such as nltk and boto3. Nltk dependency needs to be explicitly added in the lambda function, however boto3 is present by default </li>
  <li> For adding the dependency, the nltk_data and other related dependency must be added as a layer to the lambda function. This goes the same with other modules/dependencies if and when required.</li>
  <li>The json file created of the named entities will then be transfered to another s3 bucket.</li>
  <li>The second bucket will also have another lambda function associated with it, this lambda function will store the JSON file into the AWS RDS.</li>
  <li> The second lambda function requires the mysql.connector library dependency which is added as a layer to it.</li>
  
</ul> 
<h3>Points to note:</h3>
<ul>
  <li>All the logs can be watched in the CloudWatch logs that is by default associated with every lambda function.</li>
  <li>While creating the lambda function, the dependencies must be added as layer. AWS lambda only supports few libraries.</li>
  <li>Policies for full access to s3 buckets must be attached to the lambda function in the IAM roles, by default every lambda function gets lambdaexecutionroles</li>
  <li>S3 trigger must be added to the lambda function explicitly. This trigger specifies by what type of event the lambda function will be called, specify that. </li>
     
</ul>

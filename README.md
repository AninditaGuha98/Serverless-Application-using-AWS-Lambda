# Serverless-Application-using-AWS-Lambda

<h3> List of tasks: </h3>
<ul>
  <li> Uploaded 400 files from a directory one at a time to the s3 bucket created in the AWS educate account.</li>
  <li> Once a file is added to the bucket, an event must be triggered which calls a function present in AWS lambda. This lambda function converts the text file into named entities. </li>
  <li> The lambda function contains dependencies such as nltk and boto3. Nltk dependency needs to be explicitly added in the lambda function, however boto3 is present by default </li>
  <li> For adding the dependency, the nltk_data and other related dependency must be added as a layer to the lambda function. This goes the same with other modules/dependencies if and when required.</li>
  <li>The json file created of the named entities will then be transffered to another s3 bucket.</li>
</ul>  

import boto3

s3 = boto3.client("s3")

def getObject(bucket, key):
    objectBody = s3.get_object(Bucket = bucket, Key = key)
    print(objectBody["Body"].read().decode("utf-8"))
    print("\n")

print("Original object from the S3 bucket:")

getObject("tutorial-bucket",
          "tutorial.txt")
print("Object transformed by S3 Object Lambda:")


getObject("arn:aws:s3-object-lambda:us-west-1:399569570370:accesspoint/tutorial-object-lambda-access-point", "tutorial.txt")
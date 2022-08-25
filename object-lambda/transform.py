import boto3
import requests


def lambda_handler(event, context):
    object_context = event["getObjectContext"]

    s3_url = object_context["inputS3Url"]

    request_route = object_context["outputRoute"]
    request_token = object_context["outputToken"]

    response = requests.get(s3_url)
    original_object = response.content.decode("utf-8")

    transformed_object = original_object.upper()

    s3 = boto3.client("s3")

    s3.write_get_object_response(
        Body = transformed_object,
        RequestRoute = request_route,
        RequestToken = request_token
    )

    return {'status_code': 200}
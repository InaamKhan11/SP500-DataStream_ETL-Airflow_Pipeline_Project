import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

def upload_to_s3(file_path, s3_key):
    s3 = get_s3_client()
    bucket = os.getenv("S3_BUCKET")
    try:
        s3.upload_file(file_path, bucket, s3_key)
        print(f"✅ Uploaded '{file_path}' to S3 bucket '{bucket}' as '{s3_key}'")
    except Exception as e:
        print(f"❌ Failed to upload to S3: {e}")

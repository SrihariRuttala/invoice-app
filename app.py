import os

import boto3
from dotenv import load_dotenv

# Load configuration from .env
load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION", "us-east-1"),
)


def upload_invoice(file_path: str, bucket: str = "customer-invoices"):
    """Upload a generated invoice PDF to our S3 bucket."""
    s3 = session.client("s3")
    key = os.path.basename(file_path)
    s3.upload_file(file_path, bucket, key)
    print(f"Uploaded {key} to {bucket}")


def list_invoices(bucket: str = "customer-invoices"):
    s3 = session.client("s3")
    for obj in s3.list_objects_v2(Bucket=bucket).get("Contents", []):
        print(obj["Key"])


if __name__ == "__main__":
    list_invoices()

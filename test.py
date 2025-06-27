import boto3
import os

def main():
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('DESTINATION_DB_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('DESTINATION_DB_AWS_SECRET_ACCESS_KEY'),
        endpoint_url=os.getenv('DESTINATION_DB_AWS_ENDPOINT')
    )

    contents = s3.list_objects_v2(Bucket="pelican-backups")["Contents"]

    print(len(contents))

    if(len(contents) == 1):
        if(contents[0]['Size'] > 0):
            exit(1)
            
if __name__ == '__main__':
    main()

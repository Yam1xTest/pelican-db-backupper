import boto3
import os

def main():
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('DESTINATION_DB_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('DESTINATION_DB_AWS_SECRET_ACCESS_KEY'),
        endpoint_url=os.getenv('DESTINATION_DB_AWS_ENDPOINT')
    )

    objects_list = s3.list_objects_v2(Bucket="pelican-backups")
    try:
        contents = objects_list["Contents"]
        for c in contents:
            print(c['Size'], c['Key'])
    except:
        raise Exception("Bucket is empty")

    if(contents[-1]['Size'] == 0):
        raise Exception("Backup size is 0")

    if(not round((contents[-1]['Size'] / (2**10)), 1) == 687.1):
        raise Exception(f"Invalid backup size! Backup size should be 687.1. Current backup size is {round((contents[-1]['Size'] / (2**10)), 1)}")

if __name__ == '__main__':
    main()

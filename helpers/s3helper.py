import sys
import traceback

sys.path.append("../")
from Config import config
import boto3
from aiobotocore.session import get_session
import asyncio
import aiofiles

def getAllFiles(bucket,folderName):
    client= boto3.client('s3',
                              aws_access_key_id=config.getS3AccessKey(),
                              aws_secret_access_key=config.getS3SecretKey(),
                              region_name=config.getAWSRegion())
    prefix=folderName
    result = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    print(result)
    filelist=[]
    for res in result['Contents']:
        filelist.append("https://"+bucket+".s3."+config.getAWSRegion()+".amazonaws.com/"+res['Key'])
    #print(filelist)
    return filelist


def uploadFile(bucket,file_path,object_key,file_type):
    client = boto3.client('s3',
                          aws_access_key_id=config.getS3AccessKey(),
                          aws_secret_access_key=config.getS3SecretKey(),
                          region_name=config.getAWSRegion())
    resp=client.upload_file(file_path,bucket,object_key,
                            ExtraArgs={'Metadata': {'content-type': file_type}})
    return resp

async def uploadFileAsync(bucket,file_path,object_key,file_type):
    try:
        session = get_session()
        async with session.create_client('s3', region_name=config.getAWSRegion(),
                                         aws_secret_access_key=config.getS3SecretKey(),
                                         aws_access_key_id=config.getS3AccessKey()) as client:
            with open(file_path,"rb") as file_handle:
                resp=await client.put_object(Bucket=bucket,Key=object_key,Body=file_handle,ContentType= file_type)
                return resp
    except Exception as e:
        print(e)
    return None



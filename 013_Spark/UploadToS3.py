def s3_upload(file, file_name, bucket='filestoragedatabricks'):

    try:
        s3 = boto3.resource('s3')
        s3object = s3.Object(bucket, file_name)
        s3object.put(
            Body=(bytes(json.dumps(file).encode('UTF-8')))
        )
    
    except ClientError as e:
        logging.error(e)
        return False
    
    return True

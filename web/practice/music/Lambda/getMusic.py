import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('teamspeak3nosyamoji')
    bucket.download_file('music1/data.json', '/tmp/data.json')
    f=open("/tmp/data.json") #ファイルオープン
    json_data = json.load(f)
    #print(json_data)
    f.close()
    return {
        'statusCode': 200,
        'body': json.dumps(json_data, ensure_ascii=False)
    }
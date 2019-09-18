import json
import boto3
import random


def loading():
    print("loading start")
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('teamspeak3nosyamoji')
    bucket.download_file('music1/data.json', '/tmp/data.json')
    bucket.download_file('music1/data2.json', '/tmp/data2.json')
    
    f=open("/tmp/data.json") #ファイルオープン
    f2=open("/tmp/data2.json") #ファイルオープン
    
    json_data = json.load(f) #jsonに変換
    json_data2 = json.load(f2) #jsonに変換
    
    f.close()
    f2.close()
    
    while(len(json_data)!=0):
        json_data2.append(json_data.pop())
    
    f=open("/tmp/data.json","w")
    f2=open("/tmp/data2.json","w")
    
    json.dump(json_data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    json.dump(json_data2, f2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    
    print (json_data)
    f.close()
    f2.close()
    
    #こっからアップロード
    bucket.upload_file('/tmp/data.json','music1/data.json')
    bucket.upload_file('/tmp/data2.json','music1/data2.json')
    
    
    
def lambda_handler(event, context):
    # TODO implement
    loading()
    
    return {
        'statusCode': 200,
        'body': ('Hello from Lambda!')
    }

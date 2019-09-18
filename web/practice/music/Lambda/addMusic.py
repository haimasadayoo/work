import json
import boto3
import random


def loading(event):
    print("loading start")
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('teamspeak3nosyamoji')
    bucket.download_file('music1/data.json', '/tmp/data.json')
    f=open("/tmp/data.json") #ファイルオープン
    json_data = json.load(f) #jsonに変換
    print(json_data) #確認用
    #こっから追加する要素をいい感じにする
    #event は{ no*:曲名 nu*:url name:お名前}
    #これを{user: name: url: score:}の形にする
    print(event)
    print(type(event))
    m1={"user":event["name"],"name":event["no1"],"url":event["nu1"],"score":"0"}
    m2={"user":event["name"],"name":event["no2"],"url":event["nu2"],"score":"0"}
    m3={"user":event["name"],"name":event["no3"],"url":event["nu3"],"score":"0"}
    json_data.append(m1)
    json_data.append(m2)
    json_data.append(m3)
    f.close()
    f=open("/tmp/data.json","w")
    #f.write(json_str)
    random.shuffle(json_data)
    json.dump(json_data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    print (json_data)
    f.close()
    
    
    
    
    #こっからアップロード
    bucket.upload_file('/tmp/data.json','music1/data.json')
    
    
    
    
def lambda_handler(event, context):
    # TODO implement
    json=loading(event)
    
    return {
        'statusCode': 200,
        'body': ('Hello from Lambda!')
    }

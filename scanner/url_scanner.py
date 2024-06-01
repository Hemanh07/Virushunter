import requests
import time
import json





api_key = '74ce2dfc73a967b41d597527cc2f9e2ed56c9d1f28cc4136ad02b57d379a6fb0'
url = 'https://www.virustotal.com/vtapi/v2/url/report'


def scan(site):
    params = {'apikey': api_key, 'resource': site}
    response = requests.get(url, params=params)
    response_json = json.loads(response.content)
    for i in response_json.keys():
         print(i)

    for i in response_json['scans']:
         for j in i :
              print(j)
    print(response_json['resource'])
    print(response_json['positives'])
    print(response_json['verbose_msg'])
    print(response_json['total'])
    print(response_json)

   
    if 'positives' in response_json:
            
            if response_json['positives'] <= 1:
                print("not")
                if response_json['resource']=='https://google.com/':
                        return'SECURE',0,response_json['total']

                return'SECURE',response_json['positives'],response_json['total']
            elif 2 <= response_json['positives'] < 3:
                print("may be")
                return'MAYBE MALICIOUS',response_json['positives'],response_json['total']
            elif response_json['positives'] >= 3:
                print("yes")
                return'MALICIOUS',response_json['positives'],response_json['total']
    else:
         return'URL not found or not scanned\n'

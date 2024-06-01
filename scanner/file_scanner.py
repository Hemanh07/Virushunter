import os
import requests
from django.conf import settings

def scan_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
                        destination.write(chunk)
    api_key = '74ce2dfc73a967b41d597527cc2f9e2ed56c9d1f28cc4136ad02b57d379a6fb0'            
    """ 
    scan_url = "https://www.virustotal.com/vtapi/v2/file/scan"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(scan_url, files=files, params={'apikey': api_key})
    scan_id = response.json()['scan_id']
                
                # Wait for the scan to complete
    scan_report_url = f"https://www.virustotal.com/vtapi/v2/file/report?apikey={api_key}&resource={scan_id}"
    scan_report_response = requests.get(scan_report_url)
    scan_report = scan_report_response.json()
    response_json=scan_report """
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {"apikey": api_key}
    files = {"file": open(file_path, "rb")}
    print(files)

    response = requests.post(url, files=files, params=params)
    if response.status_code == 200:
        file_url = f"https://www.virustotal.com/api/v3/files/{response.json()['sha1']}"
        headers = {"accept": "application/json", "x-apikey": api_key}
        report_response = requests.get(file_url, headers=headers)
        print(report_response)
        if report_response.status_code == 200:
            print(report_response.json())
            return report_response.json()["data"]["attributes"]
        else:
            return"Failed to retrieve file report."
            
    else:
        return"Failed to scan file."
        
    """ for i in response_json.keys():
         print(i)
    if 'positives' in response_json:

        if response_json['positives'] == 0:
                        return 'NOT Malicious ',scan_report["data"]["attributes"]
        elif 1 <= response_json['positives'] < 3:
                        return 'MAYBE MALICIOUS',scan_report["data"]["attributes"]
        elif response_json['positives'] >= 3:
                        return 'MALICIOUS!',scan_report["data"]["attributes"]
    else:
            return 'file not found or not scanned\n',scan_report["data"]["attributes"]
 """

""""
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {"apikey": api_key}
    files = {"file": open(file_path, "rb")}
    print(files)

    response = requests.post(url, files=files, params=params)
    if response.status_code == 200:
        file_url = f"https://www.virustotal.com/api/v3/files/{response.json()['sha1']}"
        headers = {"accept": "application/json", "x-apikey": api_key}
        report_response = requests.get(file_url, headers=headers)

        if report_response.status_code == 200:
            print("hai")
            for i in report_response.json().keys():
                print(i)
"""
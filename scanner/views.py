import os
import requests
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from.forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .url_scanner import scan
from.file_scanner import scan_file
from .display_report import display_report
def home(request):
     return render(request,'landingpage.html')
def home_page(request):
     return render(request,'landingpage.html')

def url_result(request):
        if request.method == 'POST':
            if request.POST['text'] is not '':
                url=request.POST['text']
                print(url)
                result_,positives,total=scan(url)
                data={"url_output": True,"result":result_,"url":url,"positives":positives,"total":total}
                return JsonResponse(data)
                #return "hi".json()
                #return render (request,'url_result.html',{'url_output': True,'result':result_,'url':url,'positives':positives,'total':total})
            else: 
                data={'warning':"*please enter the valid url."}
                return JsonResponse(data)
        else:
             return render(request,'url.html',{'url_output':False})





@csrf_exempt
def upload_and_scan_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            
            report=scan_file(file)
            if type(report) is not str:
                print(report)
            # Check if the file is malicious
                size,hash,descp,result,malicious_count=display_report(report)
                print(result)
                filedata={"file_output": True,"size":size,"hash":hash,"descp":descp,"malicious_count":malicious_count}
                print(filedata)
                return JsonResponse(filedata)
         #   return render (request,'file.html',{'file_output': True,'name':file,'size':size,'hash':hash,'descp':descp,'result':result,'malicious_count':malicious_count,'verdict':verdict})
    else:
        form = UploadFileForm()
    return render(request, 'file.html', {'file_output':False,'form': form})
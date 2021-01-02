from django.shortcuts import render
from django.http import  HttpResponse
import numpy as np
from  django.http import  JsonResponse

# Create your views here.

def json_response(data,result=True,message="OK",code=0):
    return  JsonResponse(
        {
            "data":data,
            "result":result,
            "message":message,
            "code":code
        }
    )

def deduceBlue(request,*args,**kwargs):
    x=float(request.POST.get("x_para"))
    y=float(request.POST.get("y_para"))
    z=np.sqrt(x*x+y*y)
    data=dict()
    data["result"]=z

    return  json_response(data)


def pureTest(request,*args,**kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render
from app1.models import * 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
def index(request):
    obj = crudajax.objects.filter(delete_flag=False).all()
    return render(request,'index.html',{"obj":obj})

def selectPeriod123(request):
    if request.method == "GET" and request.is_ajax():
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        email = request.GET.get('email')
        password = request.GET.get('password')
        crudajax.objects.create(fname = fname,lname = lname,mymail = email, mypswd = password)

        print(fname)
        return JsonResponse({'success':'my data is saved'}, safe=False)
        # fname = request.

def UpdateDeleteView(request):
    obj = crudajax.objects.all()
    return render(request,'updatedeleteview.html',{"obj":obj})

def updateview(request):
    if request.method == "GET" and request.is_ajax():
        id = request.GET.get('ids')
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        email = request.GET.get('email')
        password = request.GET.get('password')
        crudajax.objects.filter(id = id).update(fname = fname,lname = lname,mymail = email, mypswd = password)
        return JsonResponse({'success':'my data is saved'}, safe=False)
def editview(request):
    if request.method == "GET" and request.is_ajax():
        id = request.GET.get('id')
        obj = list(crudajax.objects.filter(id = id).values())
        # obj = list(crudajax.objects.filter(id = id).values())
        # print(obj[0]['fname'])
        return JsonResponse({'obj':obj,"data":obj[0]['fname']}, safe=False)


def deleteview(request):
    if request.method == "GET" and request.is_ajax():
        id = request.GET.get('id')
        
        crudajax.objects.filter(id=id).update(delete_flag=True)
        # obj = list(crudajax.objects.filter(id = id).values())
        # print(obj[0]['fname'])
        return JsonResponse({"success":"deleted successfully"}, safe=False)
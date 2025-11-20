from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt

from .models import StudentNew,Users


# Create your views here.

data={
    'name':"Virat Kholi",
    'age':38,
    'city':"Ranchi",
    'country':"India"
}
def wish(request):
    return HttpResponse("HELLO WORLD")


def greet(request):
    return HttpResponse("WElCOME TO DJANGO.......")

def details(request):
    return JsonResponse(data)

def sampleinfo(request):
    data1={'resukt':[12,33,4445,556,66666]}
    return JsonResponse(data1 | data)



def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
            return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})



@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method=='POST':
        data=json.loads(request.body)
        student=StudentNew.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email')
        )
        return JsonResponse({'status':'success','id':student.id},status=200)
    

    elif request.method=='GET':
        result=list(StudentNew.objects.values())
        print(result)
        return JsonResponse({'status':'ok','data':result},status=200)
    

    elif request.method=='PUT':
        data=json.loads(request.body)
        ref_id=data.get("id") #geting id
        new_email=data.get("email") #getting email
        existing_student=StudentNew.objects.get(id=ref_id) #fecthing the object as the id
        # print(existing_student)
        existing_student.email=new_email #updating with new email
        existing_student.save()
        updated_data=dict(StudentNew.objects.filter(id=ref_id).values().first())
        print(updated_data)
        return JsonResponse({'req':'data updated suceesfully','updated data':updated_data},status=200)


    elif request.method=='DELETE':
        data=json.loads(request.body)
        ref_id=data.get("id") #geting id
        get_deleted_data=dict(StudentNew.objects.filter(id=ref_id).values().first())
        to_be_delete=StudentNew.objects.get(id=ref_id) 
        to_be_delete.delete()
        return JsonResponse({'req':'suceess','message':"students recored dleted",'deleted_data':get_deleted_data},status=200)
    return JsonResponse({'error':"use post method"},status=400)



def job1(request):
    return JsonResponse({"Message":"You have suceesfully apllied for job1"},status=200)

def job2(request):
    return JsonResponse({"Message":"You have suceesfully apllied for job2"},status=200)

@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        return JsonResponse({"status":"Success"},status=200)
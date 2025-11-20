from django.http import JsonResponse
import json,re
from basic.models import StudentNew, Users




class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        # print(request,'hello')
        if(request.path=="/student/"):
            print(request.method,'method')
            print(request.path)

        response=self.get_response(request)
        return response
    

 
# import json


# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response

#     def __call__(self, request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get('email')
#         dob=data.get('dob')
#         password=data.get('pswd')



class sscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        if(request.path in {'/job1/','/job2/'}):
            ssc_result=(request.GET.get("ssc"))
            if(ssc_result!="True"):
                return JsonResponse({"error":"You should qualify atleast scc for applying these job"},status=400)
        return self.get_response(request)



class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        if(request.path =='/job1/'):
            medicalFit_result=(request.GET.get("Medically_Fit"))
            if(medicalFit_result!='True'):
                return JsonResponse({"error":"You should qualify medically for applying these job"},status=400)
        return self.get_response(request)



class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        if(request.path in ['/job1/','/job2/']):
            age_result=int(request.GET.get("age",17))
            if( age_result < 18 or age_result > 25):
                return JsonResponse({"error":"Age must be in betwwen 18 and 25"},status=400)
        return self.get_response(request)
        
# http://127.0.0.1:8000/job1/?age=10&Medically_Fit=True&ssc=True


class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        if request.path=="/signup/":
            data=json.loads(request.body)
            username=data.get("username","")
            if not username:
                return JsonResponse({"Eroor":"Username is required"},status=400)
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"username should contains 3 to 20 characters"},status=400)
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should should not start or ends with . or _"},status=400)
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username should contains only letrees dots,munbers,underscores"},status=400)
            if ".." in username or "__" in username:
                return JsonResponse({"error":"cannot have .. or __"},status=400)
        return self.get_response(request)
    
class EmailMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path == "/signup/":
            data = json.loads(request.body)
            email = data.get("email", "")
            if not email:
                return JsonResponse({"error": "email is required"}, status=400)
            email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(email_regex, email):
                return JsonResponse({"error": "invalid email format"}, status=400)
            if Users.objects.filter(email=email).exists():
                return JsonResponse({"error": "email already exists"}, status=400)
        return self.get_response(request)
    





class PasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path == "/signup/":
            data = json.loads(request.body)
            password = data.get("password", "")
            
            # Check empty
            if not password:
                return JsonResponse({"error": "password is required"}, status=400)

            # No spaces allowed
            if " " in password:
                return JsonResponse({"error": "password should not contain spaces"}, status=400)

            # Minimum length
            if len(password) < 8:
                return JsonResponse({"error": "password must be at least 8 characters long"}, status=400)

            #Strong password regex
            strong_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]+$"
            if not re.match(strong_pattern, password):
                return JsonResponse({
                    "error": "password must contain uppercase, lowercase, number, and special character"
                }, status=400)
        return self.get_response(request)
            
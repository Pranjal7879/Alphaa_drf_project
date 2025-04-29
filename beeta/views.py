from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from beeta.serializers import EmployeeSerializer, UserSerializer
from .models import Employee , User , OTP
from rest_framework import status
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import cache_page
# from rest_framework_simplejwt.tokens import RefreshToken




@cache_page(60*1)
@api_view(['GET','POST'])
def office(request):
    xyz = { 
        'office' : 'GoldenEagle',
        'services' : [ 'web' , 'android', 'AI', 'ROR' ],
        'Service_Provider' : "employee"
    }
    if request.method == 'GET':
        print('comming from get request')
        print("Fetching from view, not cache")
        return Response(xyz)
    elif request.method == 'POST':
        data = request.data
        print(data)
        print('coming from a post request')
        return Response(xyz)
    elif request.method == 'PUT':
        print('coming from a put method')
        return Response(xyz)


# class officeView(APIView):
#     def get(self, request):
#         xyz = {
#             'office': 'GoldenEagle',
#             'services': ['web', 'android', 'AI', 'ROR'],
#             'Service_Provider': "employee"
#         }
#         return Response(xyz)


@api_view(['GET', 'POST'])
def employee_view(request):
    if request.method == 'GET':
        objs = Employee.objects.all()
        serializer = EmployeeSerializer(objs , many =True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)



class Signupview(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/login/')
        return Response({'message': 'user created'}, status=status.HTTP_201_CREATED)
        
        
    

class Loginview(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email: 
            return Response({'error':'Email is Required'}, status=status.HTTP_400_BAD_REQUEST) 

        try:
            user = User.objects.get(email=email)
        except:
               pass 
         
        otp = get_random_string(6, allowed_chars='0123456789')
        OTP.objects.create(user=user, otp_code=otp)

        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return Response({'message': 'otp send'},status=status.HTTP_200_OK)  
    


class VerifyOtpview(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp_enterd = request.data.get('otp')

        if not email or not otp_enterd:
            return Response({'error': 'Email & OTP are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except :
            pass

        otp_obj = OTP.objects.filter(user=user, otp_code=otp_enterd).last()

        if otp_obj:
            otp_obj.is_verified = True
            otp_obj.save()
            return Response({'message': 'Successfully logged in'}, status=status.HTTP_200_OK)
            
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


        

class Homeview(APIView):
    def get(self, request):
        return Response({'message':'succesfully login'})            
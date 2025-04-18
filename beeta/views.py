from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from beeta.serializers import EmployeeSerializer
from .models import Employee , User , OTP
from django.shortcuts import render, redirect 
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET','POST'])
def office(request):
    xyz = {
        'office' : 'GoldenEagle',
        'services' : [ 'web' , 'android', 'AI', 'ROR' ],
        'Service_Provider' : "employee"
    }
    if request.method == 'GET':
        print('comming from get request')
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


def signupview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        user = User.objects.create(name=name, email=email)

        return redirect('login')
    
    return render(request, 'signup.html')


def loginview(request):
    email = ''
    
    if request.method == 'POST':
        email = request.POST.get('email')
        otpenter = request.POST.get('otp')

        
        if 'generate_otp' in request.POST:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                otp = get_random_string(6, allowed_chars='0123456789')
                OTP.objects.create(user=user, otp_code=otp)
                send_mail(
                    'Your OTP Code',
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(request, 'login.html', {'email': email})
            else:
                return render(request, 'login.html', {'error': 'Email not registered'})

       
        elif otpenter:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                newotp = OTP.objects.filter(user=user, otp_code=otpenter).last()
                if newotp:
                    newotp.is_verified = True
                    newotp.save()
                    return redirect('/api/home/')
                else:
                    return render(request, 'login.html', {'email': email, 'error': 'invalid otp'})

    return render(request, 'login.html')

@login_required
def homeview(request):
    return render(request, 'home.html')

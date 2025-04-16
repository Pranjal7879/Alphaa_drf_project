from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework.response import Response
from beeta.serializers import EmployeeSerializer
from .models import Employee



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

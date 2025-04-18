from beeta.views import office, employee_view ,loginview,signupview,homeview
from django.urls import path

urlpatterns = [
    path('office/',office),
    path('employee/', employee_view,name='employee'),
    path('signup/',signupview,name='signup'),
    path('login/',loginview,name='login'),
    path('home/',homeview,name='home')

]



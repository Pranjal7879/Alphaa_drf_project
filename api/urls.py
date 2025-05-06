from beeta.views import office, employee_view ,Loginview,Signupview,Homeview,VerifyOtpview
from django.urls import path

urlpatterns = [
    path('office/',office),
    path('employee/', employee_view,name='employee'),
    path('signup/', Signupview.as_view(), name='signup'),
    path('login/', Loginview.as_view(), name='login'),
    path('verify-otp/', VerifyOtpview.as_view(), name='verify-otp'),
    path('home/', Homeview.as_view(), name='home'),

]



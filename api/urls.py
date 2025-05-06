from beeta.views import office, employee_view ,Loginview,Signupview,Homeview,VerifyOtpview, ProductView , Productidview,ProductCategory
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('office/',office),
    path('employee/', employee_view,name='employee'),
    path('signup/', Signupview.as_view(), name='signup'),
    path('login/', Loginview.as_view(), name='login'),
    path('verify-otp/', VerifyOtpview.as_view(), name='verify-otp'),
    path('home/', Homeview.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:id>/', Productidview.as_view(), name='product-detail'),
    path('products/<str:category>/', ProductCategory.as_view(), name='product-category'),
    path('api/products/<int:id>/', Productidview.as_view()) 
]



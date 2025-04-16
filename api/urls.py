from beeta.views import office, employee_view
from django.urls import path

urlpatterns = [
    path('office/',office),
    path('employee/', employee_view)
]



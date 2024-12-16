from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    r"employee/employee-view-set",
    EmployeeViewset,
    basename="",
)
router.register(r"employees", EmployeeViewset)

urlpatterns = [
    #path('employee/', EmployeeViewset, name='patient'),
]

urlpatterns += router.urls

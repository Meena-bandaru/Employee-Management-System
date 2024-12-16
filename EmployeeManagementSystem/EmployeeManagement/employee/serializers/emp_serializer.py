from rest_framework import serializers
from ..models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer: Employee"""

    class Meta:
        model = Employee
        fields = "__all__"

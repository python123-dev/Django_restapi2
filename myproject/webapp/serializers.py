from rest_framework import serializers
from .models import employee

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=('f_name','emp_id')
        #fields='__all__'
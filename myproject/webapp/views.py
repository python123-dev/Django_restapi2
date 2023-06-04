from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializers

# Create your views here.
class employeeList(APIView):

    def get(self,request):
        employee1=employee.objects.all()
        serializer=employeeSerializers(employee1,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = employeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Datacreated'})

    def put(self,request,pk):
        id=pk
        stu=employee.objects.get(pk=id)
        serializer = employeeSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'})


    def delet(self,request,pk):
        id=pk
        stu=employee.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})


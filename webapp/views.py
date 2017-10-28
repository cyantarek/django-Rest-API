from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeList(APIView):

	def get(self, request):
		employees = Employees.objects.all()
		serializer = EmployeeSerializer(employees, many=True)
		return Response(serializer.data)

	def post(self):
		pass

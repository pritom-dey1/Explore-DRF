# from django.shortcuts import render
# from django.http import JsonResponse
from student.models import Student
from .Serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employes.models import Employee
from .Serializers import EmployeeSerializer
from rest_framework import generics , mixins
from blog.models import Blog, Comment
from .Serializers import BlogSerializer, CommentSerializer

# Create your views here.
@api_view(['GET','POST'])
def StudentView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def StudentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class EmployeeView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
#     def post(self, request):
        
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
# class EmployeeDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return None
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data , status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class EmployeeView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class EmployeeDetailView(mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin,
#                          generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class EmployeeView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    
class BlogViewSet(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class CommentViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task  # Import your Task model
from .serializers import TaskSerializer  # Import your Task serializer
from django.contrib.auth.models import User  # Import User model for registration
from rest_framework import serializers

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()  # Logic to retrieve all tasks
        serializer = TaskSerializer(tasks, many=True)  # Serialize the tasks
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterView(APIView):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['username', 'password', 'email']

    def post(self, request):
        serializer = self.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterView(APIView):
    def post(self, request):
        # Your registration logic here
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
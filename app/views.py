from django.shortcuts import render
from .models import user
from .serializers import userserializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class userfirst(viewsets.ModelViewSet):
    '''
    This class uses ModelViewSet to perform Retrieve, Create, Update and Delete operations
    '''
    queryset=user.objects.all()                             #Takes all the objects from user
    serializer_class = userserializer
    authentication_classes = [TokenAuthentication]        #Use an in-built drf functionality for Token authentication
    permission_classes = [IsAuthenticated]                  #Assign IsAuthenticated permission which grants API access to only authorized users
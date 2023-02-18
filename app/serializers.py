from rest_framework import serializers
from django.db import models
from .models import user

class userserializer(serializers.Serializer):
    '''
    This class inherits from serializers class and defines the fields name birthdate and gender for various operations
    '''
    name = serializers.CharField()
    birthdate = serializers.DateField()
    gender = serializers.CharField(max_length=8)

    def create(self, validated_data):
        return user.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        This function takes three input arguments and stores the data entered by the user into the respective fields present in database
        '''
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate',instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
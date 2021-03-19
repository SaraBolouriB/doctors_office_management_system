from rest_framework import serializers
from .models import *

class allUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = all_users
        fields = '__all__'

class normalUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = normal_user
        fields = '__all__'

class doctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = doctor
        fields = '__all__'
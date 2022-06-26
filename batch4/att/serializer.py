from rest_framework import serializers
#from .models import MasterData

class AttSerializer(serializers.Serializer):
	stuid = serializers.IntegerField()
	stuname = serializers.CharField(max_length=100)
	stumail = serializers.EmailField(max_length=100)
	

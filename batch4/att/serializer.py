from rest_framework import serializers
from .models import MasterData2


def email_valid(value):
	if not value.endswith("xyz.com"):
		raise serializers.ValidationError("Not valid email")

class AttSerializer(serializers.Serializer):
	stuid = serializers.IntegerField()
	stuname = serializers.CharField(max_length=100)
	stumail = serializers.EmailField(max_length=100,validators=[email_valid])

	#def validate_stuid(self,value):   # Field level validation
	#	if value >=100:
	#		raise serializers.ValidationError("Not valid")
	#	return value
	'''
	def validate(self,data):   # object level validation
		stuid = data.get('stuid')
		stumail = data.get('stumail')

		if stuid >100:
			raise serializers.ValidationError("Not valid")
		if stumail.endswith("xyz.com"):
			raise serializers.ValidationError("Not valid EMAIL")

		return data 
	'''

	def create(self,validated_data):
		return MasterData2.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.stuname = validated_data.get('stuname', instance.stuname)
		instance.stumail = validated_data.get('stumail',instance.stumail)
		instance.save()
		return instance


class AttSerializer1(serializers.ModelSerializer):
	#stumail = serializers.EmailField(max_length=100,validators=[email_valid])
	class Meta:
		model = MasterData2
		fields = ['stuid','stuname','stumail']


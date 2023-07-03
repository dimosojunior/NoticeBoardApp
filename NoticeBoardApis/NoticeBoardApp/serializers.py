
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings

# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= User
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = User.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = User.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)


		


class NewsSerializer(serializers.ModelSerializer):

	class Meta:
		model = News
		fields = '__all__'





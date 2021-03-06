from rest_framework import serializers

from user.models import CustomerUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_superuser', 'phone_number', 'token')
        extra_kwargs = {'password': {'write_only': True}}

class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser')
        
class UpdateLocalTokenUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerUser
        fields = ('token', )

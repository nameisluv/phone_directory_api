from rest_framework import serializers
from .models import User, Contact, SpamReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number']

class SpamReportSerializer(serializers.ModelSerializer):
    reported_by = serializers.PrimaryKeyRelatedField(read_only=True)  # Make it read-only

    class Meta:
        model = SpamReport
        fields = ['id', 'contact_number', 'reported_by']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

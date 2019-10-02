from rest_framework import serializers
from .models import Profile, User
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        password = data['password']
        if not username:
            raise serializers.ValidationError('Username is required to login.')
        user = User.objects.filter(username=username)
        if user.exists():
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username is not valid.')
        
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect username/password')
            else:
                token = Token.objects.filter(user_id=user_obj.id).first()
                data['token'] = token
                return data
        
        data['token'] = Token.objects.create(user=user_obj) # Keep for those current user without token

        return data

class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','token']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username = username, email= email)
        user_obj.set_password(password)
        user_obj.save()
        validated_data['token'] = Token.objects.create(user=user_obj)
        return validated_data
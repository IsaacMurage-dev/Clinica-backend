from rest_framework import serializers


from .models import MedicalHistory, Profile, Sms,Vaccine,MedicalHistory,Growth

# cloudinary
from cloudinary.models import CloudinaryField
# user
from django.contrib.auth.models import User


# get all users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','date_joined')

# create user
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("profile_pic", "contact", "location", "isDctor")

# Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user_name", "parent_name", "place of birth", "contact", "location", "address", "DoB", "updated_at")

class VaccineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vaccine
        fields = ['patient','vaccine', 'brand_name', 'batch_number', 'drug_expiry', 'next_appointment', 'date_given'] 
        
         
        # growth======
class GrowthSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Growth
        fields = ['patient','age', 'weight', 'height', 'HO','date']     
    
    
    # medical history====
class MedicalHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicalHistory
        fields = ['disease_history', 'patient','doctor_recommendation']   

     #sms====     
class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = ['parent_name', 'email', 'phone']

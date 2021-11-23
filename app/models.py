from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from django.urls import reverse
from url_or_relative_url_field.fields import URLOrRelativeURLField

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.



class Vaccine(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    vaccine = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255, null=True)
    batch_number = models.CharField(max_length=50)
    drug_expiry = models.DateField()
    user_profile = CloudinaryField('image')
    next_appointment=models.CharField(max_length=50)
    date_given = models.DateField()
    

    def __str__(self):
        return f"{ self.vaccine }"




# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('image', blank=True)
    contact = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    isDoctor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"CartID : { self.pk }"

    def get_absolute_url(self):
        return reverse('vaccine_detail', kwargs={'pk': self.pk})
    
          
    
    # growth=======>
class Growth(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.DecimalField(max_digits=12, decimal_places=2)
    weight = models.DecimalField(max_digits=12, decimal_places=2)
    height = models.DecimalField(max_digits=12, decimal_places=2)
    HO = models.IntegerField()
    date = models.DateField()
    

    def __str__(self):
        return f"{ self.patient.username }"
    
    def get_absolute_url(self):
            return reverse('', kwargs={'pk': self.pk})


# medical disease==============>
class MedicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_history = models.TextField(max_length=200)
    doctor_recommendation = models.TextField(max_length=200)
    

    def __str__(self):
        return f"{ self.disease_history }"

    # def get_absolute_url(self):
    #     return reverse('disease_detail', kwargs={'pk': self.pk})
# sms model
class Sms(models.Model):
    parent_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
   
    
from django.contrib import admin
from .models import Profile,Growth,MedicalHistory,Vaccine
# Register your models here.


admin.site.register(Profile)
admin.site.register(Growth)
admin.site.register(MedicalHistory)
admin.site.register(Vaccine)

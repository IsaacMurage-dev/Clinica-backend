from django.contrib import admin
from .models import Profile,Growth,EmergingDisease,Vaccine
# Register your models here.


admin.site.register(Profile)
admin.site.register(Growth)
admin.site.register(EmergingDisease)
admin.site.register(Vaccine)

from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # api
   
    url(r'^api/profiles/$', views.ProfileList.as_view()), # list of profiles
    url(r'^api/profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()), # single profile
    url(r'^api/users/$', views.UserList.as_view()), # list of users
    url(r'^api/users/create/$', views.UserCreate.as_view()), # create user
    url(r'^api/auth/login/$', views.loginUser.as_view()), # login user
    url(r'^api/auth/logout/$', views.logoutUser.as_view()), # logout user
    url(r'^api/vaccine/$', views.VaccineList.as_view(), name="vaccines"),
    url(r'^api/medicalhistory/$', views.MedicalHistoryList.as_view(), name="medicalHistory"),
    url(r'^api/growth/$', views.GrowthList.as_view(), name="growth"),
    url(r'^api/vaccines/<int:pk>/', views.VaccineDetail.as_view(), name="vaccines_detail"),
    url(r'^api/send-message',views.SendSmsMessage.as_view(),name="sms-message")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from . import views
from django.urls import path

urlpatterns=[
    path('create_user/',views.user_register,name="user_creation"),
    path("verify_otp/",views.user_verification,name="verify_otp"),
    path("otp_renewal/",views.otp_renewal,name="renewel_of_otp"),
]
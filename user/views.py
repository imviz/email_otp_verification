from rest_framework.decorators import api_view
from .models import User,EmailOtp
from rest_framework.response import Response
from rest_framework  import status
from .serailizer import UserSerializer,EmailOtpSerializer
from .otp_gen import otp_generation
from .mail_senter import send_email
from datetime import datetime


@api_view(["POST"])
def user_register(request):
    try:
        details=request.data
        email=details["email"]
        exists=User.objects.filter(email=email).exists()
        if exists:
            message={'error':'email exists'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        user=User.objects.create(first_name=details["first_name"],last_name=details["last_name"],email=details["email"],password=details["password"])
        otp=otp_generation()
        EmailOtp.objects.create(email=user,otp=otp)
        recipient_email = 'changeme'
        subject = 'Test Email'
        body = f'your One Time Password is \n {otp} .Dont share this otp to any one'        
        send_email(recipient_email, subject, body, )
        seri=UserSerializer(user,many=False)
        return Response(seri.data)
    except:
        pass



@api_view(["POST"])
def user_verification(request):
    try:
        details=request.data
        email=details["email"]
        otp=details["otp"]
        user=User.objects.filter(email=email).first()
        if not user:
            message={'error':'No record found in this email'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        elif user.is_active is True:
            message={'success':'already verified'}
            return Response(message,status=status.HTTP_200_OK)
        user_otps=EmailOtp.objects.filter(email=user).all().order_by("-id")
        latest_otp=user_otps[0]
        otp_time_and_date=latest_otp.create_at
        current_time_and_date =datetime.now()
        otp_date=otp_time_and_date.date()
        otp_time=otp_time_and_date.time()
        updated_otp_time_and_date=datetime.combine(otp_date,otp_time)
        experied= current_time_and_date - updated_otp_time_and_date
        if experied.seconds > 60:
            message={'error':'your otp experied please renew you otp'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)        
        if int(otp) != latest_otp.otp:
            message={'error':'incorrect otp'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST) 
        verified_user=User.objects.filter(email=user.email).first()
        verified_user.is_active =True
        verified_user.save()
        message={'success':'you are verified successfully'}
        return Response(message,status=status.HTTP_200_OK)
    except:
        pass
        

@api_view(["POST"])
def otp_renewal(request):
    try:
        details=request.data
        email=details["email"]
        user=User.objects.filter(email=email).first()
        if not user:
            message={'error':'email exists'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        otp=otp_generation()
        EmailOtp.objects.create(email=user,otp=otp)
        recipient_email = 'changeme'
        subject = 'Test Email'
        body = f'your One Time Password is \n {otp} .Dont share this otp to any one'        
        send_email(recipient_email, subject, body, )
        message={'success':'otp sented to your mail success fully'}
        return Response(message,status=status.HTTP_200_OK)
    except:
        pass

from rest_framework import serializers, exceptions
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _
import re
import random
import redis

from app_user.models import User


class SignupSerializer(serializers.ModelSerializer):
    default_error_messages = {
        "invalid_email": {
            "status": False,
            "message": 'لطفا ایمیل معتبر وارد کنید'
        }
    }

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name'
        )

    def __init__(self, *args, **kwargs):
        super(SignupSerializer, self).__init__(*args, **kwargs)

        self.fields["password"].validators = [MinLengthValidator(8, message=_("پسورد باید حداقل ۸ کاراکتر و ترکیبی از حروف و اعداد باشد"))]
        self.fields["password"].error_messages["required"] = u"ارسال پسورد اجباری است"
        self.fields["password"].error_messages["blank"] = u"پسورد نباید خالی باشد"

    def validate_email(self, value):
        email = re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', value)
        if email is None:
            raise exceptions.ParseError(
                self.error_messages['invalid_email'], 'invalid_email'
            )

        user = User.objects.filter(email=value.lower()).first()
        if user:
            raise exceptions.ParseError({
                'status': False,
                "message": 'این ایمیل قبلا ثبت شده است'
            })
        return value.lower()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        otp_code_length = 5
        otp_code = str(random.randint((10 ** (otp_code_length - 1)), (10 ** otp_code_length - 1)))

        rds = redis.StrictRedis(decode_responses=True, host='localhost', port=6379, db=0)
        rds.set(f"{user.email}_otp_code_signup", otp_code)
        rds.expire(f"{user.email}_otp_code_signup", 60 * 30) # 30min
        user.send_email({
            "title": "فعالسازی ثبت نام",
            "code": otp_code
        })

        return True

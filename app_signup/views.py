from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app_signup.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=self.request.data)
        if ser.is_valid():
            ser = ser.save()
            return Response({
                "status": True,
                "message": "ثبت نام شما با موفقیت انجام شد و کد فعالسازی به ایمیل شما ارسال گردید"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "message": ser.errors[list(ser.errors)[0]][0]
            }, status=status.HTTP_400_BAD_REQUEST)


class AccountActivationView(generics.CreateAPIView):
    # serializer_class = AccountActivationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=self.request.data)
        if ser.is_valid():
            ser = ser.save()
            return Response({
                "status": True,
                "message": "حساب کاربری شما فعال شد"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "message": ser.errors[list(ser.errors)[0]][0]
            }, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate
from rest_framework import serializers

# def get_and_authenticate_user(email,password):
#     user=authenticate(username=email,password=password)
#     if user is None:
#         raise serializers.ValidationError("چنین کاربری وجود ندارد")
#
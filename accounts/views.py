from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


from rest_framework.permissions import AllowAny


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.contrib.auth import authenticate
from django.db import transaction

from 
# Create your views here.

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from App_auth.serializers import *
from App_auth.models import *

# Create your views here.
class RegistrationAPIView(CreateAPIView):
    # allow any user (authenticated or not) to access the endpoint
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        # create a serializer with the incoming data
        serializer = self.serializer_class(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # create a new user
            user = serializer.save()
            # send a registration email
            # return a successful response
            return Response({"success": f"Successfully registered!!!"}, status=status.HTTP_201_CREATED)
        else:
            # Return a validation error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    def post(self, request, *args, **kwargs):
        # create a serializer with the incoming data
        serializer = self.serializer_class(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # create a company
            user = serializer.save()
            # send a registration email
            # return a successful response
            return Response({"success": f"Comany Setup successful!!!"}, status=status.HTTP_201_CREATED)
        else:
            # Return a validation error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

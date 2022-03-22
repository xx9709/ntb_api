from django.shortcuts import render
from .serializers import UserSerializer, GetMoneySerilizer
from rest_framework.views import APIView
from rest_framework.response import Response


class AddUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetMoneyView(APIView):
    def post(self, request):
        serializer = GetMoneySerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


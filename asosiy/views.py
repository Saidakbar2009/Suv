from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *

# Create your views here.
class SuvlarAPiView(APIView):
    def get(self, request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)
        return Response(serializer.data)

    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True"})
        return Response(serializer.errors)

    def update(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True"})
        return Response(serializer.errors)

class MijozlarApiView(APIView):
    def get(self, request):
        mijoz = Mijoz.objects.all()
        serializer = MijozSerializer(mijoz, many=True)
        return Response(serializer.data)

    def post(self, request):
        mijoz = request.data
        serializer = SuvSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True"})
        return Response(serializer.errors)

    def post(self, request):
        mijoz = request.data
        serializer = SuvSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True"})
        return Response(serializer.errors)

class SuvApiView(APIView):
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response({"success":"True"})

class MijozApiView(APIView):
    filter_backends = [SearchFilter]
    search_fields = ['ism', 'tel']

    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response({"success":"True"})

class BuyurtmaApiView(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BuyurtmaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"success":"True"})

class AdminlarApiView(APIView):
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class HaydovchilarApiView(APIView):
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = AdminSerializer(haydovchi, many=True)
        return Response(serializer.data)

class AdminApiView(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

class HaydovchiApiView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)
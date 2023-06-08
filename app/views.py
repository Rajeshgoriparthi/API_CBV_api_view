from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
class ProductData(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PCJD=ProductSerializers(PQS,many=True)
        return Response(PCJD.data)

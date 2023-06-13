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
    def get(self,request,id):
        PQS=Product.objects.all()
        PCJD=ProductSerializers(PQS,many=True)
        return Response(PCJD.data)


    def post(self,request,id):
        PMSD=ProductSerializers(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'massages':'Product is created'})
        else:
            return Response({'massages':'Product is failed'})


    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UDO=ProductSerializers(PO,data=request.data)
        if UDO.is_valid():
            UDO.save()
            return Response({'massages':'Product is updated'})
        else:
            return Response({'massages':'Product is failed'})


    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UDO=ProductSerializers(PO,data=request.data,partial=True)
        if UDO.is_valid():
            UDO.save()
            return Response({'massages':'Product is parcially updated'})
        else:
            return Response({'massages':'Product is failed'})


    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'massage':'product is deleted'})
    
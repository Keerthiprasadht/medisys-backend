# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Hospital
from .serializers import HospitalSerializer
from rest_framework.decorators import api_view

@swagger_auto_schema(
    method='post',  # corrected 'metthod' to 'method'
    tags=['Hospital'],
    operation_id="create_hospital",
    request_body=HospitalSerializer,
    responses={201: HospitalSerializer, 400: 'Bad Request'},
    operation_summary="Create a new hospital",
    operation_description="Creates a new hospital and returns its details"
)
@api_view(['POST'])
def create_hospital(request):
    serializer = HospitalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get hospitals
@swagger_auto_schema(
    method='get',
    tags=['Hospital'],
    operation_id="get_hospitals",
    responses={200: HospitalSerializer(many=True), 404: 'Not Found'},
    operation_summary="Get all hospitals",
    operation_description="Returns a list of all hospitals"
)
@api_view(['GET'])
def get_hospitals(request):
    hospitals = Hospital.objects.all()
    serializer = HospitalSerializer(hospitals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

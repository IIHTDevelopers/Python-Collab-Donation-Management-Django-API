from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NGOSerializer,DonorSerializer,DonationSerializer,DonationRequestSerializer
from .models import NGOModel,DonorModel,DonationModel,DonationRequestModel
from .exceptions import InvalidData,IdNotAvailable

class NGOView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonorView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonorWithNGOView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonationView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonationByDonarView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationForNGOView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationRequestView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationRequestByNGOView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

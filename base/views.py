from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from base.serializers import (
    FolderSerializer
)

# Create your views here.
class HandleFileUpload(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = FolderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'file upload successfully',
                })

            return Response({
                'status':400,
                'message':'something went wrong',
                'error':serializer.errors
            })
        
        except Exception as e:
            print(e)


from django.shortcuts import render
from .models import Video
from .serializers import VideoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

import sys
import errno


# Create your views here.
class VideoView(APIView):
    class Upload(generics.CreateAPIView):
        # permission_classes = [CanContracts]
        queryset = Video.objects.all()
        serializer_class = VideoSerializer

        def post(self, request, *args, **kwargs):
            print('THIS IS REQUEST', request.data)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class List(generics.ListAPIView):
        queryset = Video.objects.all()
        serializer_class = VideoSerializer

        def post(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            queryset = queryset.filter(title__icontains=request.data['title'])
            serializer = VideoSerializer(queryset, many=True)
            return Response(serializer.data)

        def get(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = VideoSerializer(queryset, many=True)
            return Response(serializer.data)

    class Get(generics.RetrieveAPIView):
        # queryset = Video.objects.get(pk=kwargs['pk'])
        queryset = Video.objects.all()
        serializer_class = VideoSerializer
        lookup_field = 'pk'

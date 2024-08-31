from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagView(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all().order_by('name')
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

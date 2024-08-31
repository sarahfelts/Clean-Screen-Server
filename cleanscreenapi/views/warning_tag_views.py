from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import WarningTag

class WarningTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningTag
        fields = '__all__'

class WarningTagView(viewsets.ViewSet):
    def list(self, request):
        queryset = WarningTag.objects.all().order_by('id')
        serializer = WarningTagSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WarningTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = WarningTag.objects.all()
        warning_tag = get_object_or_404(queryset, pk=pk)
        serializer = WarningTagSerializer(warning_tag)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = WarningTag.objects.all()
        warning_tag = get_object_or_404(queryset, pk=pk)
        warning_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

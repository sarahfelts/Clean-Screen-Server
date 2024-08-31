from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import WarningDetail

class WarningDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningDetail
        fields = '__all__'

class WarningDetailView(viewsets.ViewSet):
    def list(self, request):
        queryset = WarningDetail.objects.all().order_by('name')
        serializer = WarningDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WarningDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = WarningDetail.objects.all()
        warning_detail = get_object_or_404(queryset, pk=pk)
        serializer = WarningDetailSerializer(warning_detail)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = WarningDetail.objects.all()
        warning_detail = get_object_or_404(queryset, pk=pk)
        serializer = WarningDetailSerializer(warning_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

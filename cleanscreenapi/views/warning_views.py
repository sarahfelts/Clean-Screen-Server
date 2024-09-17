from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import WarningIterable

class WarningIterableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningIterable
        fields = '__all__'

class WarningIterableView(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]  # Require user to be authenticated
    
    def list(self, request):
        queryset = WarningIterable.objects.all().order_by('timestamp')
        serializer = WarningIterableSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = WarningIterableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = WarningIterable.objects.all()
        warning = get_object_or_404(queryset, pk=pk)
        serializer = WarningIterableSerializer(warning)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = WarningIterable.objects.all()
        warning = get_object_or_404(queryset, pk=pk)
        serializer = WarningIterableSerializer(warning, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = WarningIterable.objects.all()
        warning = get_object_or_404(queryset, pk=pk)
        warning.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

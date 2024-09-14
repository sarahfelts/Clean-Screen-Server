from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import WarningIterable
from cleanscreenapi.firebase_setup import verify_firebase_token

class WarningIterableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningIterable
        fields = '__all__'

class WarningIterableView(viewsets.ViewSet):
    def list(self, request):
        queryset = WarningIterable.objects.all().order_by('timestamp')
        serializer = WarningIterableSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        id_token = auth_header.split('Bearer ')[1]
        decoded_token = verify_firebase_token(id_token)
        if decoded_token is None:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
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

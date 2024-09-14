from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import SavedMovie
from cleanscreenapi.firebase_setup import verify_firebase_token

class SavedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMovie
        fields = '__all__'

class SavedMovieView(viewsets.ViewSet):
    def list(self):
        queryset = SavedMovie.objects.all().order_by('id')
        serializer = SavedMovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        id_token = auth_header.split('Bearer ')[1]
        decoded_token = verify_firebase_token(id_token)
        if decoded_token is None:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = SavedMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        id_token = auth_header.split('Bearer ')[1]
        decoded_token = verify_firebase_token(id_token)
        if decoded_token is None:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = SavedMovie.objects.all()
        saved_movie = get_object_or_404(queryset, pk=pk)
        saved_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import SavedMovie

class SavedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMovie
        fields = '__all__'

class SavedMovieView(viewsets.ViewSet):
    def list(self, request):
        queryset = SavedMovie.objects.all().order_by('id')
        serializer = SavedMovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SavedMovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = SavedMovie.objects.all()
        saved_movie = get_object_or_404(queryset, pk=pk)
        serializer = SavedMovieSerializer(saved_movie)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = SavedMovie.objects.all()
        saved_movie = get_object_or_404(queryset, pk=pk)
        saved_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

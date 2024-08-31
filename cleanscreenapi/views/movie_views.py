from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from cleanscreenapi.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieView(viewsets.ViewSet):
    def list(self, request):
        queryset = Movie.objects.all().order_by('title')
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import SavedMovie
from cleanscreenapi.forms import SavedMovieForm

def create_saved_movie(request):
    if request.method == 'POST':
        form = SavedMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_movie_list')
    else:
        form = SavedMovieForm()
    return render(request, 'saved_movie_form.html', {'form': form})

def saved_movie_list(request):
    saved_movies = SavedMovie.objects.all()
    return render(request, 'saved_movie_list.html', {'saved_movies': saved_movies})

def delete_saved_movie(request, saved_movie_id):
    saved_movie = get_object_or_404(SavedMovie, id=saved_movie_id)
    if request.method == 'POST':
        saved_movie.delete()
        return redirect('saved_movie_list')
    return render(request, 'confirm_delete.html', {'object': saved_movie})

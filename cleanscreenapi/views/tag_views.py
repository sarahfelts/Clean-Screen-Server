from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import Tag
from cleanscreenapi.forms import TagForm

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tag_form.html', {'form': form})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

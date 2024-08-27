from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import WarningTag
from cleanscreenapi.forms import WarningTagForm

def create_warning_tag(request):
    if request.method == 'POST':
        form = WarningTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warning_tag_list')
    else:
        form = WarningTagForm()
    return render(request, 'warning_tag_form.html', {'form': form})

def warning_tag_list(request):
    tags = WarningTag.objects.all()
    return render(request, 'warning_tag_list.html', {'tags': tags})

def delete_warning_tag(request, tag_id):
    tag = get_object_or_404(WarningTag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        return redirect('warning_tag_list')
    return render(request, 'confirm_delete.html', {'object': tag})

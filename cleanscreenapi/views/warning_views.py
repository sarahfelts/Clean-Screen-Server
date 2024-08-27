from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import WarningIterable
from cleanscreenapi.forms import WarningForm

def create_warning(request):
    if request.method == 'POST':
        form = WarningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warning_list')
    else:
        form = WarningForm()
    return render(request, 'warning_form.html', {'form': form})

def warning_list(request):
    warnings = WarningIterable.objects.all()
    return render(request, 'warning_list.html', {'warnings': warnings})

def warning_detail(request, warning_id):
    warning = get_object_or_404(WarningIterable, id=warning_id)
    return render(request, 'warning_detail.html', {'warning': warning})

def update_warning(request, warning_id):
    warning = get_object_or_404(WarningIterable, id=warning_id)
    if request.method == 'POST':
        form = WarningForm(request.POST, instance=warning)
        if form.is_valid():
            form.save()
            return redirect('warning_detail', warning_id=warning.id)
    else:
        form = WarningForm(instance=warning)
    return render(request, 'warning_form.html', {'form': form})

def delete_warning(request, warning_id):
    warning = get_object_or_404(WarningIterable, id=warning_id)
    if request.method == 'POST':
        warning.delete()
        return redirect('warning_list')
    return render(request, 'confirm_delete.html', {'object': warning})

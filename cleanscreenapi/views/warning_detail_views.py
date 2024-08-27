from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import WarningDetail
from cleanscreenapi.forms import WarningDetailForm

def create_warning_detail(request):
    if request.method == 'POST':
        form = WarningDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warning_detail_list')
    else:
        form = WarningDetailForm()
    return render(request, 'warning_detail_form.html', {'form': form})

def warning_detail_list(request):
    details = WarningDetail.objects.all()
    return render(request, 'warning_detail_list.html', {'details': details})

def update_warning_detail(request, detail_id):
    detail = get_object_or_404(WarningDetail, id=detail_id)
    if request.method == 'POST':
        form = WarningDetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('warning_detail_list')
    else:
        form = WarningDetailForm(instance=detail)
    return render(request, 'warning_detail_form.html', {'form': form})

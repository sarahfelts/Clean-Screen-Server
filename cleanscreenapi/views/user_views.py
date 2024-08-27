from django.shortcuts import render, get_object_or_404, redirect
from cleanscreenapi.models import User
from cleanscreenapi.forms import UserCreationForm, UserChangeForm

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'user_form.html', {'form': form})

def read_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

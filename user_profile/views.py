# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages

@login_required
def profile(request):
    user = request.user
    return render(request, 'user_profile/profile.html', {'user': user})
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Redirect to user profile page after saving
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'user_profile/edit_profile.html', {'form': form})
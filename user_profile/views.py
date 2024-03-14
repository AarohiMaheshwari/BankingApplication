# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm
from .models import ProfilePicture

@login_required
def profile(request):
    user = request.user
    try:
        profile_picture = ProfilePicture.objects.get(user=user)
    except ProfilePicture.DoesNotExist:
        profile_picture = None

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data['profile_picture']
            if profile_picture:
                profile_picture.picture = picture
                profile_picture.save()
            else:
                ProfilePicture.objects.create(user=user, picture=picture)
            return redirect('profile')
    else:
        form = ProfilePictureForm()

    return render(request, 'user_profile/profile.html', {'user': user, 'form': form, 'profile_picture': profile_picture})

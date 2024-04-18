# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CardApplicationForm

@login_required
def apply_for_card(request):
    if request.method == 'POST':
        form = CardApplicationForm(request.POST)
        if form.is_valid():
            card_application = form.save(commit=False)
            card_application.user = request.user
            card_application.save()
            return redirect('card_application_success')
    else:
        form = CardApplicationForm()
    return render(request, 'cards/apply_for_card.html', {'form': form})

@login_required
def card_application_success(request):
    return render(request, 'cards/card_application_success.html')


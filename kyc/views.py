# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import KYCDocumentForm

@login_required
def upload_kyc_document(request):
    if request.method == 'POST':
        form = KYCDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document_name = form.cleaned_data['document_name']
            kyc_document = form.save(commit=False)
            kyc_document.user = request.user
            kyc_document.save()
            return redirect('kyc_document_success')
    else:
        form = KYCDocumentForm()
    return render(request, 'kyc/upload_kyc_document.html', {'form': form})

@login_required
def kyc_document_success(request):
    return render(request, 'kyc/kyc_document_success.html')

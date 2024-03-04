# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .forms import KYCDocumentForm
from .models import KYCDocument
from django.contrib.auth.models import User


@login_required
def upload_kyc_document(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = KYCDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            kyc_document = form.save(commit=False)
            kyc_document.user = user
            kyc_document.save()
            return redirect('kyc_document_success')
    else:
        form = KYCDocumentForm()
    return render(request, 'kyc/upload_kyc_document.html', {'form': form})

@login_required
def kyc_document_success(request):
    return render(request, 'kyc/kyc_document_success.html')

def retrieve_kyc_documents(request, user_id):
    user = User.objects.get(pk=user_id)
    kyc_documents = KYCDocument.objects.filter(user=user)
    return render(request, 'kyc/kyc_doc_list.html', {'kyc_documents': kyc_documents, 'user': user})
    

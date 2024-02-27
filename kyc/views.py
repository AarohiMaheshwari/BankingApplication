# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import KYCDocumentForm
from .models import KYCDocument

@login_required
def upload_kyc_document(request):
    if request.method == 'POST':
        form = KYCDocumentForm(request.POST, request.FILES)
        if form.is_valid():
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

def retrieve_kyc_documents(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        kyc_documents = KYCDocument.objects.filter(account_number=account_number)
        return render(request, 'kyc/kyc_doc_list.html', {'kyc_documents': kyc_documents, 'account_number': account_number})
    else:
        return render(request, 'kyc/retrieve_docs.html')

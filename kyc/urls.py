# urls.py

from django.urls import path
from .views import upload_kyc_document, kyc_document_success, retrieve_kyc_documents

urlpatterns = [
    path('upload-kyc-document/', upload_kyc_document, name='upload_kyc_document'),
    path('kyc-document-success/', kyc_document_success, name='kyc_document_success'),
    path('retrieve_documents/', retrieve_kyc_documents, name='retrieve_kyc_documents'),
]

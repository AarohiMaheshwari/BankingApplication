# urls.py

from django.urls import path
from .views import admin_dashboard, upload_kyc_document, kyc_document_success

urlpatterns = [
    path('upload-kyc-document/', upload_kyc_document, name='upload_kyc_document'),
    path('kyc-document-success/', kyc_document_success, name='kyc_document_success'),
    path('admin_dashboard/', admin_dashboard),
]

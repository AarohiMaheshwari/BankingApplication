# urls.py

from django.urls import path
from .views import apply_for_card, card_application_success

urlpatterns = [
    path('apply-for-card', apply_for_card, name='apply_for_card'),
    path('card-application-success', card_application_success, name='card_application_success'),
]

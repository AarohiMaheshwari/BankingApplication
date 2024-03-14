# views.py

from django.shortcuts import render
from django.db import connection

def search_accounts(request):
    if request.method == 'POST':
        bank_account_id = request.POST.get('bank_account_id')
        if bank_account_id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM auth_user WHERE id = %s", [bank_account_id])
                users = cursor.fetchall()
            return render(request, 'search/search_results.html', {'users': users})
        else:
            # Handle case where bank_account_id is not provided
            return render(request, 'search/search_users.html', {'error_message': 'Please provide a bank account ID'})
    else:
        # Render the search form for GET request
        return render(request, 'search/search_users.html', {})

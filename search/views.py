# views.py

from django.shortcuts import render
from django.db import connection
from django.utils.safestring import mark_safe

def search_accounts(request):
    if request.method == 'POST':
        bank_account_id = mark_safe(request.POST.get('bank_account_id'))
        if bank_account_id:
            with connection.cursor() as cursor:
                query = f"select * from auth_user where id = {bank_account_id}"
                # cursor.execute("SELECT * FROM auth_user WHERE id = %s", [bank_account_id])
                cursor.execute(query)
                users = cursor.fetchall()
            return render(request, 'search/search_results.html', {'users': users})
        else:
            # Handle case where bank_account_id is not provided
            return render(request, 'search/search_users.html', {'error_message': 'Please provide a bank account ID'})
    else:
        # Render the search form for GET request
        return render(request, 'search/search_users.html', {})

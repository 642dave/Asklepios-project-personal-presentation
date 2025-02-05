from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request, 'accounts/accounts.html')

def privacy_policy(request):
    return render(request, 'accounts/privacy_policy.html')
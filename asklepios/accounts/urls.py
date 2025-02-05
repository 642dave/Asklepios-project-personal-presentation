from django.urls import path
from . import views

# registered application name
app_name = 'accounts' 

urlpatterns = [
    path('accounts/', views.accounts, name='accounts'),
    path('accounts/privacy_policy', views.privacy_policy, name='privacy_policy')
]

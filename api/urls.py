from django.urls import path
from .views import RegisterView, LoginView, ContactListView, ContactDetailView, MarkSpamView, SearchByNameView, SearchByPhoneView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('spam/', MarkSpamView.as_view(), name='mark-spam'),
    path('search/name/', SearchByNameView.as_view(), name='search-by-name'),
    path('search/phone/', SearchByPhoneView.as_view(), name='search-by-phone'),
]

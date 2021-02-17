from django.urls import path
from .views import (
                  IndexView,
                  about,
                  contact,
                DetailView,
)


urlpatterns = [
   path('', IndexView.as_view(), name='home'),
   path('about/', about, name='about'),
   path('contact/', contact, name='contact'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
]

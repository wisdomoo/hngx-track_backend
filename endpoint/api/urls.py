from django.urls import path
from api.views import get_info

urlpatterns = [
    path('api/', get_info, name='get_info'),
]

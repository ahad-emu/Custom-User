from users.views import CustomUserView
from django.urls import path

urlpatterns = [
    path('signup/', CustomUserView.as_view(), name='signup'),
]

# ----------------------------------------------
# users/urls.py
# URL Mappings for the users app.
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    # EN: We use the already made auth_views from django for authentication
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

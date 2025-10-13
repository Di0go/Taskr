# ----------------------------------------------
# taskr/urls.py
# URL Mappings for the main web app.
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('projects/', include('projects.urls')),

    # EN: Mapping for the auth URLs
    path('users/', include('users.urls')),
    path('login/', lambda request: redirect('users:login')),
    path('logout/', lambda request: redirect('users:logout')),
    path('register/', lambda request: redirect('users:register')),

    # EN: Redirect form / to /projects
    path('', lambda request: redirect('/projects')),

]

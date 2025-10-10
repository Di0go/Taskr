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

    # PT: Mapping dos URLs de autenticação
    path('users/', include('users.urls')),
    path('login/', lambda request: redirect('users:login')),
    path('logout/', lambda request: redirect('users:logout')),
    #path('register/', lambda request: redirect('users:register')),

    # PT: Redirecionamos o / diretamente para o /projects/
    path('', include('projects.urls')),

]

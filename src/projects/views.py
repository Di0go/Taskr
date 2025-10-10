# ----------------------------------------------
# projects/views.py
# Views for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# EN: Decorator for views that checks that the user is logged in, redirecting to the log-in page if necessary as defined in te 'settings.py'
@login_required
def index(request):
    return render(request, "projects/index.html")

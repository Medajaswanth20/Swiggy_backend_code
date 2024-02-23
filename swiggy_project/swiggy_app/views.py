 #swiggy_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Milestone

@login_required
def milestone_view(request):
    milestone = Milestone.objects.get_or_create(user=request.user)[0]
    return render(request, 'index.html', {'user': request.user, 'milestone': milestone})

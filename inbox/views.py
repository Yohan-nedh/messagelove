from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import*



@login_required
def inbox_view(request):
    return render(request, 'inbox/inbox.html')

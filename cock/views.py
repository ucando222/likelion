from django.shortcuts import render

from .models import Cock

# Create your views here.

def cock(request):
    cocks = Cock.objects
    return render(request, 'cock.html', {'cocks':cocks})

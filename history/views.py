from django.shortcuts import render
from .models import History

# Create your views here.

def history(request):
    history = History.objects.filter(status=1).order_by('id')
    context = {'history': history}
    return render(request, "history/index.html", context)
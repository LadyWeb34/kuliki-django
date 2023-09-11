from django.shortcuts import render, get_object_or_404
from .models import People

# Create your views here.

def people(request):
    people = People.objects.filter(status=1)
    context = {'people': people}
    return render(request, 'people/index.html', context)
def detail_page(request, pk):
    people = get_object_or_404(People, pk=pk)
    images = people.peopleimagelist_set.all()
    context = {
        'people': people,
        'images': images
    }
    return render(request, 'people/detail-page.html', context)
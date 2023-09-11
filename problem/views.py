from django.shortcuts import render, get_object_or_404
from .models import Problem

# Create your views here.

def problem(request):
    problem = Problem.objects.filter(status=1)
    context = {'problems': problem}
    return render(request=request, template_name='problem/index.html', context=context)

def detail_page(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    images = problem.problemimageitem_set.filter(status=1)
    context = {
        'problem': problem,
        'images': images
    }
    return render(request=request, template_name='problem/detail-page.html', context=context)
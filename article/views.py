from django.shortcuts import render
from .models import Article

def vue_test(request):
    info = Article.objects.all()
    return render(request, 'index.html', {
        'info': info,
    }, content_type='text/html')

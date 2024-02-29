from django.shortcuts import render
from django.http import HttpResponse
from lxml import etree

# Create your views here.

def home_view(request):
    title = 'Welcome to Django'
    return render(request, 'a_sxm/home.html', {'title': title})

def upload_xml(request):
    print(request)
    if request.method == 'POST'and request.FILES.get('file'):
        file = request.FILES.get('file')
        content = file.read().decode('utf-8')
        print(content)

    return render(request, 'a_sxm/home.html', {'content': content})

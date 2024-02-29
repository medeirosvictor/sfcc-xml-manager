from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from lxml import etree
from .models import *

# Create your views here.

def home_view(request):
    xmls = XML.objects.all()
    form = XMLUploadForm()
    return render(request, 'a_sxm/home.html', {'xmls': xmls, 'form': form})

def xml_view(request, xml_id):
    xml = XML.objects.get(id=xml_id)
    return render(request, 'a_sxm/xml.html', {'xml': xml})

class XMLUploadForm(forms.Form):
    file_content = forms.FileField()

def upload_xml(request):
    if request.method == 'POST':
        form = XMLUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.cleaned_data['file_content']
            file_content = file.read().decode('utf-8')
            file_name = file.name
            print(file_content)
            print(file_name)
            return render(request, 'a_sxm/xmlmanager.html', {'file_content': file_content})
        else:
            return HttpResponse('Invalid form')
    else:
        return HttpResponse('Invalid request')

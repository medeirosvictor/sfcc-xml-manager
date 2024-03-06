from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from lxml import etree
from .models import *
from io import StringIO, BytesIO

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
            file = form.cleaned_data['file_content']
            file_content = file.read()
            try:
                root = etree.fromstring(file_content)
                #root = etree.getroot()
                #print(file_content)
                namespace = root.nsmap.get(None)
                print(namespace)
                return  render(request, 'a_sxm/xmlmanager.html', {'file_content': file_content})
            except etree.XMLSyntaxError as e:
                return HttpResponse('XMLerror')
        else:
            return HttpResponse('Invalid form')
    else:
        return HttpResponse('Invalid request')
    

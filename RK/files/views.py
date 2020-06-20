from django.shortcuts import render
from .models import Catalog, File
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


def index(request):
    catalog_list = Catalog.objects.all()
    file_list = File.objects.all()
    return render(request, 'list.html', {'catalog_list': catalog_list, 'file_list': file_list})


def file(request, id):
    try:
        f = File.objects.get(id=id)
    except:
        raise Http404("Файл не найден")

    return render(request, 'file.html', {'file': f})


def create(request):
    f = File.objects.create(name=request.POST['name'], text=request.POST['text'], extension=request.POST['extension'],
                            catalog=Catalog.objects.get(name=request.POST['catalog']))
    catalog_list = Catalog.objects.all()
    file_list = File.objects.all()
    return render(request, 'list.html', {'catalog_list': catalog_list, 'file_list': file_list})


def delete_file(request, id):
    f = File.objects.get(id=id)
    f.delete()
    catalog_list = Catalog.objects.all()
    file_list = File.objects.all()
    return render(request, 'list.html', {'catalog_list': catalog_list, 'file_list': file_list})


def edit_file(request, id):
    f = File.objects.get(id=id)
    return render(request, 'edit.html', {'file': f})


def edit_done(request, id):
    f = File.objects.get(id=id)
    f.name = request.POST['name']
    f.text = request.POST['text']
    f.extension = request.POST['extension']
    f.pub_date = request.POST['pub_date']
    f.catalog = Catalog.objects.get(name=request.POST['catalog'])
    return render(request, 'file.html', {'file': f})


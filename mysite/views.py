from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog

def index(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    artikel_base = ArtikelBlog.objects.all()
    print(artikel)
    print(request.user)

    context = {
        "title":"selamat datang",
        "kategori":kategori,
        "artikel":artikel,
        "artikel_base":artikel_base,
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect ('not_found_artikel')
   
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)
    artikel_base = ArtikelBlog.objects.all()

    context = {
        "title":"selamat datang",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya,
        "artikel_base":artikel_base,
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "artikel_not_found.html"
    return render(request, template_name)

def kontak(request):
    template_name = "kontak.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def galeri(request):
    template_name = "galeri.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"selamat datang"
    }
    return render(request, template_name, context)


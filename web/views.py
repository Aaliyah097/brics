from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, "index.html", {})

def news_view(request):
    return render(request, "views/NewsView.html", {})

def events_view(request):
    return render(request, "views/EventsView.html", {})

def preferences_view(request):
    return render(request, "views/PrefencesView.html", {})

def partners_view(request):
    return render(request, "views/PartnersView.html", {})

def representatives_view(request):
    return render(request, "views/RepresentativesView.html", {})

def structure_view(request):
    return render(request, "views/StructureView.html", {})

def about_view(request):
    return render(request, "views/AboutView.html", {})

def news_detail_view(request, news_id):
    template_name = f"components/news/news-{news_id}.html"
    try:
        return render(request, template_name, {"news_id": news_id})
    except:
        raise Http404("Новость не найдена")
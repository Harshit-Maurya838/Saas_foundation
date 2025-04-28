from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def homePageView(request):
    visits = PageVisit.objects.filter(path=request.path) 
    my_context = {
        "Page_Title": "Home Page",
        "Page_Visits": visits.count()
    }
    PageVisit.objects.create(path=request.path)
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html', my_context)

def aboutPageView(request):
    visits = PageVisit.objects.filter(path=request.path) 
    my_context = {
        "Page_Title": "About Page",
        "Page_Visits": visits.count()
    }
    PageVisit.objects.create(path=request.path)
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html', my_context)
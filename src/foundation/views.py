from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def homePageView(request):
    visits = PageVisit.objects.all() 
    my_context = {
        "Page_Title": "Home Page",
        "Page_Visits": visits.count()
    }
    PageVisit.objects.create()
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html', my_context)
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

LOGIN_URL = settings.LOGIN_URL

def homePageView(request):
    visits = PageVisit.objects.filter(page=request.path) 
    my_context = {
        "Page_Title": "Home Page",
        "Page_Visits": visits.count()
    }
    PageVisit.objects.create(page=request.path)
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html', my_context)

def aboutPageView(request):
    visits = PageVisit.objects.filter(page=request.path) 
    my_context = {
        "Page_Title": "About Page",
        "Page_Visits": visits.count()
    }
    PageVisit.objects.create(page=request.path)
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html', my_context)

VALID_CODE = "abc123"

def pw_protected_view(request):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})

@login_required
def user_only_view(request):
    return render(request, "protected/user-only.html", {})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request):
    return render(request, "protected/user-only.html", {})
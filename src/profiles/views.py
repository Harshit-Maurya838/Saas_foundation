from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

@login_required
def profile_list(request):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, 'profiles/list.html', context)

@login_required
def profile_view(request, username=None):
    user = request.user
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    return HttpResponse(f"Hello There {username} - {profile_user_obj.id} - {user}")

@login_required
def profile_detail_view(request, username=None):
    user = request.user
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me
    }
    return render(request, "profiles/detail.html", context)
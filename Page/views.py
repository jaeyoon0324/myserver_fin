from django.shortcuts import render
from .models import Mypage
# Create your views here.
def landing(request):
    return render(
    request,
    'Page/landing.html'
)


def about_me(request):
    data = Mypage.objects.first()
    return render(
    request,
    'Page/about_me.html',
    {'data' : data }
)
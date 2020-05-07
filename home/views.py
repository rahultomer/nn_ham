from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "template1.html")


def expression(request):
    count = int(request.GET['count'])
    count = count-1
    a = request.GET['vec1']
    b = request.GET['vec2']
    c = request.GET['vec3']
    print(count)
    return render(request, "t2.html", {'result': a+'#'+b+'#'+c})

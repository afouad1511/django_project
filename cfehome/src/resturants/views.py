import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    bool_var = True
    some_list = [random.randint(1, 100000000), random.randint(1, 100000000), random.randint(1, 100000000)]
    context = {"bool_var": bool_var,
     "some_list": some_list
     }
    return render(request, "home.html", context)
def about(request):
    bool_var = True
    some_list = [random.randint(1, 100000000), random.randint(1, 100000000), random.randint(1, 100000000)]
    context = {"bool_var": bool_var,
     "some_list": some_list
     }
    return render(request, "about.html", context)
def contact(request):
    bool_var = True
    some_list = [random.randint(1, 100000000), random.randint(1, 100000000), random.randint(1, 100000000)]
    context = {"bool_var": bool_var,
     "some_list": some_list
     }
    return render(request, "contact.html", context)

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(request):
    """Define a view to show the 'home.html' template."""
    # the template to which we will delegate the work
    template = "bankrec/home.html"
    # a dict of key/value pairs, to be available for use in template
    context = {
        "current_time": 123,
        "letter1": 31,
        "letter2": 14,
        "number": 2,
    }
    return render(request, template, context)

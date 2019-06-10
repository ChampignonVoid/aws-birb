from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

# Create your views here.
def index(request):
    """Renders the index page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'registration/index.html',
        {
            'title':'Index Page',
            'year':datetime.now().year,
        }
    )
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import redirect,render_to_response


def landingpage(request):
    return render(request, 'LandingPage/LandingPage.html')

    #return render_to_response("Templates/index.html", RequestContext(request))
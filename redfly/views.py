# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
  """
    TODO:
      1. Show connect to gmail
      2. And a description

  """
  data = {}


  
  return render_to_response("redfly/home.html", data, context_instance=RequestContext(request))


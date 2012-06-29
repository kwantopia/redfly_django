# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import json

def home(request):
  data = {}

  if request.user.is_authenticated():
    data["output"] = "User is authenticated"
  else:
    data["output"] = "User is not authenticated"

  return render_to_response("main/home.html", data, context_instance=RequestContext(request))

def connect_gmail(request):
  """
    Authenticate through Gmail and pull header information
  """
  data = {}
  u = request.user

  u.authenticate()
  u.login()
  return render_to_response("main/connect_gmail.html", data, context_instance=RequestContext(request))

@login_required
def classify(request):
  data = {}
  return render_to_response("main/classify.html", data, context_instance=RequestContext(request))

@login_required
def classify_person(request):
  """
    Save information about a person
  """
  data = {}
  return render_to_response("main/classify_person.html", data, context_instance=RequestContext(request))

@login_required
def save_contact(request):
  data = {}
  return render_to_response("main/save_contact.html", data, context_instance=RequestContext(request))

@login_required
def search_contact(request):
  data = {}
  return render_to_response("main/search_contact.html", data, context_instance=RequestContext(request))

@login_required
def search(request):
  data = {}
  return render_to_response("main/search.html", data, context_instance=RequestContext(request))

@login_required
def profile(request):
  """
    Profile of each member on Redfly
    - people can edit their own comments, or add social media links
  """
  data = {}
  return render_to_response("main/profile.html", data, context_instance=RequestContext(request))

@login_required
def tag(request):
  """
    Tag a member with particular term 
    - people can edit tags 
    - ajax call
    - log those people who added those tags
  """
  data = {}

  data["result"] = "tagging successful"

  return HttpResponse(json.dumps(data), mimetype="application/json") 

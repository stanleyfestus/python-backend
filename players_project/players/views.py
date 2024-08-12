from django.shortcuts import HttpResponse
from django.template import  loader
from .models import Player


# Create your views here.

def players(request):
  myplayers = Player.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'myplayers': myplayers,
  }
  return HttpResponse(template.render(context, request))
from datetime import datetime
from django.shortcuts import render
import os
import time
# Create your views here.

def home(request):
    context = {"ts":datetime.now()}
    return render(request, 'home.html', context)

def listing(request):
    context = {'dir_content': os.listdir("/var/log"), "dir_name": "/var/log"}
    return render(request, 'listing.html', context)

def listing(request, paths):
  lidir = []
  for fd in os.listdir('/var/log/' + str(paths)):
    if os.path.isdir('/var/log/' + str(paths) + '/' + fd):
      templ = '<tr><td><a href="' + str(fd) + '/">' + fd + '</a></td>'
    else:
      templ = '<tr><td>' + fd + '</td>'
    templ = templ + '<td>' + str(os.path.getsize('/var/log/' + str(paths) + '/' + fd)) + '</td>'
    templ = templ + '<td>' + str(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(os.path.getmtime('/var/log/' + str(paths) + '/' + fd)))) + '</td></tr>'
    lidir.append(templ)
  context = {u'dir_content':lidir, 'dir_name': "var/log"}
  return render(request, 'listing.html', context)

from django.shortcuts import render
import time, os
# Create your views here.

def home(request):
  context = {u'ts':time.time(),}
  return render(request, 'home.html', context)

def listing(request, diry):
  lidir = []
  for fd in os.listdir('/var/log/' + str(diry)):
    if os.path.isdir('/var/log/' + str(diry) + '/' + fd):
      templ = '<tr><td><a href="' + str(fd) + '/">' + fd + '</a></td>'
    else:
      templ = '<tr><td>' + fd + '</td>'
    templ = templ + '<td>' + str(os.path.getsize('/var/log/' + str(diry) + '/' + fd)) + '</td>'
    templ = templ + '<td>' + str(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(os.path.getmtime('/var/log/' + str(diry) + '/' + fd)))) + '</td></tr>'
    lidir.append(templ)
  context = {u'dir_content':lidir,}
  return render(request, 'listing.html', context)

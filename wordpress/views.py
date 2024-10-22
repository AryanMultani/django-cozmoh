from django.shortcuts import render
from .models import Site


def site_install(request):
  return render(request, 'install_plugins.html' )

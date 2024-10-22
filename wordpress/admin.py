from django.contrib import admin
from .models import Site
from django.contrib import messages


import requests

class Plugin(admin.ModelAdmin):
  def install_plugin(self, request, obj, form, change):
    # messages.success(request, 'Site saved successfully')
    # messages.info(request, f'{obj.site_url} saved successfully')


    # check if the obj.site_url is valid. it should return a 200 status code
    try:
      response=requests.get(obj.site_url)
      response.raise_for_status()
      messages.success(request,'Holaaaaaa')
      super().save_model(request, obj, form, change)

    except requests.exceptions.RequestException:
      return messages.error(request,"Error occured, Do check your provided data")



    # login to the site using the username and password


    # check if the login is successful


    # if login is successful, start installing plugins
        # show some installation progress JS

    # display success message after installation



admin.site.register(Site, Plugin)

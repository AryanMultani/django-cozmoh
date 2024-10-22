from django.contrib import admin
from .models import Doc


class DocAdmin(admin.ModelAdmin):
  list_display = ('title', 'link')
  search_fields = ('title', 'link')


admin.site.register(Doc, DocAdmin)

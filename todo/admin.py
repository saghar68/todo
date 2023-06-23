from django.contrib import admin
from .models import TODO


class PostAdmin(admin.ModelAdmin):
    list_display=('title','text','created','status')

admin.site.register(TODO,PostAdmin)






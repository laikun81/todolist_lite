from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('message','create_date',)
    list_display_links=('message','create_date',)

admin.site.register(Post,PostAdmin)
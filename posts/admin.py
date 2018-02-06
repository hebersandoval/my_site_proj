from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    # '__unicode__' refers to the 'title' attribute and can be substituted
    list_display = ['__unicode__', 'timestamp', 'updated']
    list_display_links = ['__unicode__']
    list_filter = ['timestamp', 'updated']
    search_fields = ['title', 'content']
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

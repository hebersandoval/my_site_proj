from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # url(r'^posts/$', '<app_name>.views.<function_name>'),
    url(r'^$', 'posts.views.post_home'),
]
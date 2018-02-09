from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
def upload_location(obj, filename):
    """will upload the file to /media_cdn/<obj.id>/<filename.jpg>"""
    # filebase, extension = filename.split('.')
    # return '%s/%s.%s' %(obj.id, obj.id, extension) # will look like this: /media_cdn/3/3.jpg
    return '%s/%s' %(obj.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True, 
            width_field='width_field', 
            height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # used in python 3
    def __str__(self):
        return self.title

    # used in python 2
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'id': self.id})
        # return '/posts/%s/' %(self.id)

    class Meta:
        ordering = ['-timestamp', '-updated']

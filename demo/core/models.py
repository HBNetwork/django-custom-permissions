from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    class Meta:
        permissions = (
            ('core.blog.rename', 'Can rename title.'),
            ('core.blog.publish', 'Can publish post.')
        )
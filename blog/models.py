from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img/', default=False)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % Post.title

    def get_absolute_url(self):
        return reverse('blog.views.port', args=[self.slug])

from django.db import models
from django.urls import reverse


class News(models.Model):

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()    
    photo = models.ImageField(blank=True, upload_to="news_photos/%Y/%m/%d", default=None)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
    
        return reverse('news:news_detail', args=[self.id])













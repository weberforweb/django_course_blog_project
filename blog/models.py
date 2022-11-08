from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    STATUES_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUES_CHOICES, max_length=3)

    def __str__(self):
        return f'{self.title}: {self.author}'

    def get_absolute_url(self):
        return reverse('post_list')

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)
 
class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.DRAFT)
    
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DB', 'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length = 100, default= "")
    # status = models.CharField(max_length = 2, choices=Status.choices, default=Status.DRAFT)
    # published = PublishedManager()
    # objects = models.Manager()
    # draft = DraftManager()
    # objects = models.Manager()
    def __str__(self):
        return self.title
    
    

      
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class PublishedMeneger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Public)


class Category(models.Model):
    name = models.CharField(max_length=256)
    direction = models.SlugField(max_length=512)

    def __str__(self):
        return self.name
class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF' , 'Draft'
        Public = 'PB','Public'
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=512)
    body = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=256 , choices=Status.choices , default=Status.Draft)

    objects = models.Manager()
    published = PublishedMeneger()

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse("view" , args =[self.id])

class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.name

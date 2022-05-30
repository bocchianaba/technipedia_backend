from .products import Product
from django.db import models
from .models import User

class Project(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    is_deleted = models.BooleanField(default=False)
    product=models.ManyToManyField(Product, related_name='products', blank=True)
    services=models.TextField(blank=True, verbose_name='Services')
    difference_with_existence=models.TextField(blank=True, verbose_name='Difference with existents products and services')
    added_value=models.CharField(max_length=255, blank=True)
    created=models.BooleanField(default=False)
    patented=models.BooleanField(default=False)
    like=models.ManyToManyField(User, related_name='likes_project', blank=True)
    dislike=models.ManyToManyField(User, related_name='dislikes_project', blank=True)
    love=models.ManyToManyField(User, related_name='loves_project', blank=True)
    slug=models.CharField(max_length=255, blank=True, default='Sous titre du projet')


    class Meta:
        verbose_name = 'Project idea'
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.title
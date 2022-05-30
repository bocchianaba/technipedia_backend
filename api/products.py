from django.db import models
from pytz import country_names
from .models import User

country_choices=((value, value) for key,value in country_names.items())
sector_choices=(
    ('Agriculture','Agriculture'),
    ('Elevage','Elevage'),
    ('Bois','Bois'),
    ('Minerai','Minerai'),
)

class Product(models.Model):

    name = models.CharField(max_length=255)
    slug=models.CharField(max_length=255, blank=True, default='Sous titre du produit')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    is_deleted = models.BooleanField(default=False)
    is_basic=models.BooleanField(default=False)
    is_sector=models.BooleanField(default=False)
    is_category=models.BooleanField(default=False)
    country=models.CharField(max_length=50, blank=True, choices=country_choices)
    importation_value = models.DecimalField(verbose_name="importation value in dollars",max_digits=20, decimal_places=2, default=0)
    exportation_value = models.DecimalField(verbose_name="exportation value in dollars",max_digits=20, decimal_places=2, default=0)
    sector=models.CharField(max_length=50, blank=True, choices=sector_choices)
    parent_product=models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    transformation=models.CharField(max_length=255, blank=True)
    fabrication_method=models.TextField(blank=True, verbose_name='Fabrication method')
    services=models.TextField(blank=True, verbose_name='Services')
    difference_with_existence=models.TextField(blank=True, verbose_name='Difference with existents products and services')
    added_value=models.CharField(max_length=255, blank=True)
    created=models.BooleanField(default=False)
    patented=models.BooleanField(default=False)
    like=models.ManyToManyField(User, related_name='likes', blank=True)
    dislike=models.ManyToManyField(User, related_name='dislikes', blank=True)
    love=models.ManyToManyField(User, related_name='loves', blank=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name
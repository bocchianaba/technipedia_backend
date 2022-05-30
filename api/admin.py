from django.contrib import admin

from .project import Project

from .models import  User 
from .products import Product

admin.site.register(User)
admin.site.register(Product) 
admin.site.register(Project) 

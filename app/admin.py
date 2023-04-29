from django.contrib import admin
from .models import Customer, Product, Requirments
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Requirments)
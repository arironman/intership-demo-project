from django.contrib import admin
from Product.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price', 'created_at', 'updated_at')
    search_fields = ('name__startswith', 'price')

    fieldsets = (
        ('Product Details', {'fields': ('name', 'weight', 'price')}),
        ('Important Dates', {'fields':('created_at', 'updated_at')}),
        
    )

    readonly_fields = ['created_at', 'updated_at']

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='Product Name', max_length=100)
    weight = models.FloatField(verbose_name='Weight(in Kgs)')
    price = models.FloatField(verbose_name='Price(in Rupees)')
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True,)
    updated_at = models.DateTimeField(verbose_name='Last Updated at', auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def autocomplete_search_fields():
        return 'self.name'

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    details = models.CharField(max_length=100, null=True)
    source = models.URLField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    variant_id = models.IntegerField(default=0)
    quantity = models.IntegerField(null=True, default=0)
    price = models.IntegerField(default=0)
    sku = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=10)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.variant_id)


class ProductImage(models.Model):
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    source = models.URLField(max_length=200, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.source)

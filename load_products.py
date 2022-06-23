import json

from django.core.management.base import BaseCommand

from products.models import (
    Category,
    Product,
    ProductImage,
    ProductVariant,
    Vendor
)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as json_file:
            list_of_products = json.load(json_file)

        for single_product_info in list_of_products:
            product_category, created = Category.objects.get_or_create(name=single_product_info.get('category'))
            product_vendor, created = Vendor.objects.get_or_create(name=single_product_info.get('vendor'))

            product, created = Product.objects.get_or_create(
                title=single_product_info.get('title'), category_id=product_category.id, vendor_id=product_vendor.id,
                details=single_product_info.get('details'), source=single_product_info.get('src')
            )
            [
                ProductVariant.objects.create(
                    variant_id=product_variant.get('id'), quantity=product_variant.get('inventory_quantity'),
                    price=product_variant.get('price'), sku=product_variant.get('sku'),
                    size=product_variant.get('title'), product_id=product.id
                )
                for product_variant in single_product_info.get('available-sizes')
            ]
            [
                ProductImage.objects.create(
                    width=product_image.get('width'), product_id=product.id,
                    height=product_image.get('height'), source=product_image.get('src')
                )
                for product_image in single_product_info.get('images')
            ]
        

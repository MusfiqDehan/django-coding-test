from django.contrib import admin
from product.models import Variant, Product, ProductImage, ProductVariant, ProductVariantPrice


class VariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active',
                    'created_at', 'updated_at')
    list_filter = ('title', 'description', 'active',
                   'created_at', 'updated_at')
    search_fields = ('title', 'description', 'active',
                     'created_at', 'updated_at')
    ordering = ('title', 'description', 'active', 'created_at', 'updated_at')


admin.site.register(Variant, VariantAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'description', 'created_at', 'updated_at')


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'file_path', 'created_at', 'updated_at')


admin.site.register(ProductImage, ProductImageAdmin)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'variant_title', 'created_at', 'updated_at')


admin.site.register(ProductVariant, ProductVariantAdmin)


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('product_variant_one', 'product_variant_two', 'product_variant_three',
                    'price', 'stock', 'product', 'created_at', 'updated_at')


admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)

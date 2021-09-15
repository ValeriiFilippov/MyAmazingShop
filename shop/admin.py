from django.contrib import admin
from shop.models import Category, Product
from .models import Post, Comment

class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug")
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "available",
        "create_date",
        "update_date",
    ]
    fieldsets = ((None, {"fields": ("name",
                                    "category",
                                    "price",
                                    #"image",
                                    "available",
                                    "description")}),
                 ('Slug', {"fields": ("slug",)})
                 )

    list_filter = ["available", "create_date"]
    prepopulated_fields = {"slug": ("name",)}




# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')
# admin.site.register(Comment, CommentAdmin)
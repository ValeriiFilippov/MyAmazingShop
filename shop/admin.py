from django.contrib import admin
from shop.models import Category, Product, Comment

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
                                    "image",
                                    "available",
                                    "description")}),
                 ('Slug', {"fields": ("slug",)})
                 )

    list_filter = ["available", "create_date",]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "text"]
    list_filter = ["created", "approved"]
    search_fields = ("created", "email", "text",)



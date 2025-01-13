from django.contrib import admin

from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]


class CategoriesInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInLine,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

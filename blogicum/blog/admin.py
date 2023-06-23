from django.contrib import admin
from .models import Post, Location, Category

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )

    list_display = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )

    list_display = (
        'name',
    )


admin.site.register(Location, LocationAdmin)

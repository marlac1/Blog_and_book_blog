from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, Category

#admin.site.register(BlogPost)
#admin.site.register(Category)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published", "author", "word_count")
    empty_value_display = "Inconnu"
    list_editable = ("published",)
    search_fields = ("title","slug", )
    list_filter = ("published",)
    autocomplete_fields = ("category",)
    filter_horizontal = ("category",)
    #list_per_page = 2
    # list_display_links = ("date",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category",)


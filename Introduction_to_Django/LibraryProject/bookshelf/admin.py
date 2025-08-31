from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)



# @admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters to the sidebar
    list_filter = ('author', 'publication_year')

    # Add a search bar
    search_fields = ('title', 'author')
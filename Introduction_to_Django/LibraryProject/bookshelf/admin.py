from .models import Book
from django.contrib import admin


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
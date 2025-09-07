from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name',)



admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
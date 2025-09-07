from .models import Author, Book, Library, Librarian
import django
import os

# Setup Django environment (important for standalone scripts)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

# from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author_name = "George Orwell"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nThe librarian for {library_name} is {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


if __name__ == "__main__":
    run_queries()
  
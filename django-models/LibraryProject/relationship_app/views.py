from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: Show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("list")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})




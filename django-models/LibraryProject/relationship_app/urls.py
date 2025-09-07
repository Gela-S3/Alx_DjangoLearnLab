from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
     path('books/', list_books, name='list_books'),  # Function-based view  
     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
     path("register/", views.register, name="register"),
     path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
     path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
     path("admin-view/", views.admin_view, name="admin_view"),
     path("librarian-view/", views.librarian_view, name="librarian_view"),
     path("member-view/", views.member_view, name="member_view"),
]
   
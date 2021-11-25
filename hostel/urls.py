from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path("student/", views.Author, name="student"),
    path("student-list/", views.Studentlist, name='student-list'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]
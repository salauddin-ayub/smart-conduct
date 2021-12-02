from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path("food/", views.food, name="food"),
    path("student/", views.Author, name="student"),
    path("student-list/", views.Studentlist, name='student-list'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("products/", views.products, name='products'),
    path("order-list/", views.order_list, name='order-list'),
    path('create-order/', views.createOrderForm, name='create-order'),
    path('update-order/<str:pk>/', views.updateOder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),

]
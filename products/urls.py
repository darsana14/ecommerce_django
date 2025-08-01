from django.urls import path

from products import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.getProducts),
    path("<int:id>", views.getProduct),
    path("create", views.createProduct),
    path("delete/<int:id>", views.deleteProduct),
]
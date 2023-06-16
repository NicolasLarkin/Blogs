from category import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryCreateListView.as_view()),
    path('<int:pk>/', views.CategoryDetailView.as_view()),

]
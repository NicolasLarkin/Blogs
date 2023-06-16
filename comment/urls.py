from comment import views
from django.urls import path

urlpatterns = [
    path('', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),

]

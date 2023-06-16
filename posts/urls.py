from posts import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.PostListCreateView.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view()),

]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account import views
from dj_rest_auth.views import LoginView, LogoutView
from account.views import CustomLogoutView

router = DefaultRouter()
router.register('', views.UserViewSet)


urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', CustomLogoutView.as_view()),
    # path('', views.UserListView.as_view()),
    # path('<int:pk>/', views.UserDetailView.as_view()),
    path('', include(router.urls)),
]


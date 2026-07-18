from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'matches', views.MatchViewSet, basename='match')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', views.register, name='register'),
    path('matches/<int:match_id>/join/', views.join_match, name='join-match'),
    path('matches/<int:match_id>/leave/', views.leave_match, name='leave-match'),
]
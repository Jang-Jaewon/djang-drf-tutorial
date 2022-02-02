from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) 

urlpatterns = [
    # path('public/', views.PublicPostListAPIView.as_view()),
    path('public/', views.public_post_list),
    path('public/<int:pk>/', views.public_post_detail),
    path('', include(router.urls)),
]
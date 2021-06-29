from django.contrib import admin
from django.urls import include, path
from shortener import views
from rest_framework import routers

# router to handle all the url routing
router = routers.DefaultRouter(trailing_slash=False)
# separate /s and /create patterns for getting and posting
router.register(r's', views.URLViewSet, basename='short_url')
router.register(r'create', views.URLViewSet, basename='create_url')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

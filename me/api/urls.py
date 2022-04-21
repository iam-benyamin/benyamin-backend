from django.urls import path, include
from rest_framework import routers
from me.api.views import AboutViewSet, WorkViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet)
router.register(r'about', AboutViewSet)
router.register(r'work', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

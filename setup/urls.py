from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pbsf.views import VacinaViewSet

router = DefaultRouter()
router.register(r'vacinas', VacinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

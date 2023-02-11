
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CoursesViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'courses', CoursesViewSet, basename='courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

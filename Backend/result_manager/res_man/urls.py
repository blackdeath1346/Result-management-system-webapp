from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from res_man.views import StudentViewSet,CourseViewSet,EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)




#print("hello")
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

   # path()
]



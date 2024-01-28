from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tasks/', include("tasks.urls")),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
# [COPY & IMPLEMENT]
# colab_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Forward all base requests to blog.urls
    path('', include('blog.urls')),
]

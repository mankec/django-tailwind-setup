from django.contrib import admin
from django.urls import include, path

from example_app import views as example_app_views

urlpatterns = [
    path("", example_app_views.index, name="index"), # Root
    path("example_app/", include("example_app.urls")),
    path("admin/", admin.site.urls),
]

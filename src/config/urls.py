from django.contrib import admin
from django.urls import include, path

from core.views import DispoHomePage, Error404

urlpatterns = [
    path("", DispoHomePage.as_view(), name='index'),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("mongo/", include("mongo_dispo.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = Error404.as_view()

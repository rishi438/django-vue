from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("account.urls")),
    path("api/post/", include("post.urls")),
    path("api/search/", include("search.urls")),
    path("api/chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

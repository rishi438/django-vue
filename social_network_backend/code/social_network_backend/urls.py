from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("code.account.urls")),
    path("api/post/", include("code.post.urls")),
    path("api/search/", include("code.search.urls")),
    path("api/chat/", include("code.chat.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

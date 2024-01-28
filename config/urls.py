from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='home')),
    path('users/', include('users.urls', namespace='user')),
    path('mailing/', include('mailing.urls', namespace='mailing')),
    path('blog/', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


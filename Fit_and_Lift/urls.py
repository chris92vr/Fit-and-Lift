from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('membership/', include('membership.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('static/<path:path>/', serve,
         {'document_root': settings.STATIC_ROOT, }),
    path('media/<path:path>/', serve,
         {'document_root': settings.MEDIA_ROOT, }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

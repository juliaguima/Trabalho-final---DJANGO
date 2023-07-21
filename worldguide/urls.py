from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('africa/', include('africa.urls')),
    path('america/', include('america.urls')),
    path('asia/', include('asia.urls')),
    path('europa/', include('europa.urls')),
    path('oceania/', include('oceania.urls')),
    path('usuario/', include('usuario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
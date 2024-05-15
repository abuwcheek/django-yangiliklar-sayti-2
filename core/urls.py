from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('kechirasiz/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('', include('apps.home.urls'))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Vanya'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('covid_helper.urls')),
    path('blog/', include('blog.urls')),
    ]
# ]
# static(settings.STATIC_URL, document_root=settings.STATICFILES_DIR)


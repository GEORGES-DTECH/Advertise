
from django.contrib import admin
from django.urls import path, include

from album.views import Photohomeview

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('root/', admin.site.urls),
    path('', Photohomeview.as_view(), name='photohome'),
  
    path('accounts/', include('accounts.urls')),
    path('album/', include('album.urls')),
    path('blog/', include('blog.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

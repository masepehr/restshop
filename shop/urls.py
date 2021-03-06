from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from content.views import add_category,get_brands

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/',include('content.urls')),
    path('',include('content.urls')),
    path('users/',include('users.urls')),
    path('cart/',include('cart.urls')),
    path('shipping/',include('shipping.urls')),
    path('payment/',include('payment.urls')),
    path('search/',include('search.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

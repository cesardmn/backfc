from django.contrib import admin
from django.urls import path, include
from products.views import ItemViewSet
from order.api.viewsets import OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

admin.site.site_header = 'Fogão Caseiro'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Fogão Caseiro'

from django.urls import path
from .views import product_detail,product_in_category
from django.conf import settings
from django.conf.urls.static import static


app_name = 'item'


urlpatterns = [
    path('',product_in_category,name='product_all'),
    path('<slug:category_slug>/',product_in_category,name='product_in_category'),
    path('<int:id>/<slug:product_slug>/',product_detail,name='product_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



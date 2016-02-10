from django.conf.urls import url

urlpatterns = [
     url(r'^$', 'products.views.index', name='index'),
     url(r'^(?P<id>[0-9]+)/$', 'products.views.product_page', name="product_page"),
         ]

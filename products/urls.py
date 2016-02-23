from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'products.views.index', name='index'),
	url(r'^(?P<id>[0-9]+)/$', 'products.views.product_page', name="product_page"),
	url(r'^add/(?P<product_id>[0-9]+)', 'products.views.add_to_cart', name="add_to_cart"),
	url(r'^remove/(?P<product_id>[0-9]+)', 'products.views.remove_from_cart', name="remove_from_cart"),
	url(r'^cart/$', 'products.views.cart', name='cart'),
	url(r'^cart/checkout/', 'products.views.checkout', name='checkout'),
         ]

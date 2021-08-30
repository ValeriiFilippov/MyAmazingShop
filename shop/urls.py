from django.urls import path
from django.conf.urls import url
from shop import views
from .views_example import ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]

urlpatterns += [
    url(r'^product/create/$', ProductCreate.as_view(), name='product_create'),
    url(r'^product/(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^product/(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='product_delete'),
]

from django.conf.urls import include, url

urlpatterns = [
    url(r'^address-book/', include('simple_address_book.urls')),
    url(r'^$', 'simple_address_book.views.home'),
]

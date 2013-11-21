from django.conf.urls import patterns, include, url
from orders.views import CustomersList, CustomerDetails

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^library/$', 'books.views.books'),
    url(r'^library/books/$', 'books.views.books'),
    url(r'^library/books/(\d+)/$', 'books.views.book'),
    url(r'^library/authors/$', 'books.views.authors'),
    url(r'^library/authors/(\d+)/$', 'books.views.author'),
    url(r'^orders/$', CustomersList.as_view()),
    url(r'^orders/(?P<pk>\d+)/$', CustomerDetails.as_view(template_name="orders/customer.html")),
    # Examples:
    # url(r'^$', 'imgs.views.home', name='home'),
    # url(r'^imgs/', include('imgs.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

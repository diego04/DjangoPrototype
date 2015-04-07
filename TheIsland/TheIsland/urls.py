from django.conf.urls import include, url, patterns
from django.contrib import admin
from login import views

urlpatterns = patterns('',

    #all-auth in the /admin thing
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', views.landingpage, name = 'landingpage'),

    # Examples:
    # url(r'^$', 'TheIsland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #from tutorial
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    )

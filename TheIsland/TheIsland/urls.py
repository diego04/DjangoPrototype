from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',

    #all-auth in the /admin thing
    (r'^accounts/', include('allauth.urls')),

    # Examples:
    # url(r'^$', 'TheIsland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    )

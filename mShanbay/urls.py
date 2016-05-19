from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from account import views as account_views



urlpatterns = [
    # Examples:
    # url(r'^$', 'mShanbay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from account import views as account_views
from eatwords import views as eatwords_views


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$',account_views.login,name='login'),
    url(r'^logout/$',account_views.logout,name='logout'),
    url(r'^join/$',account_views.join,name='join'),

    url(r'^$',eatwords_views.index, name='index'),
    url(r'eating/',eatwords_views.eating, name='eating'),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()

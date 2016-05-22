from django.conf.urls import include, url
from eatwords import views as eatwords_views
urlpatterns = [
    url(r'^$',eatwords_views.eating, name='eating'),
    # url(r'^note/$',eatwords_views.note, name='note'),
    url(r'^note/api/$',eatwords_views.note_api, name='note_api'),
]

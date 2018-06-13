from django.urls import path
from . import views

urlpatterns = [
    
    path(r'', views.MusicList.as_view(), name='music-list'),

    path(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),
    
    path(r'^albuns/$', views.AlbumList.as_view()),

    path(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),

    path('^bands/$', views.BandList.as_view()),

    path(r'^band/(?P<pk>[0-9]+)/$', views.BandDetail.as_view()),

    path(r'^members/$', views.MemberList.as_view()),

    path(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    
]
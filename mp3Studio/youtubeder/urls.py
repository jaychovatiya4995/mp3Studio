from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('FAQ', views.faqs, name='faqs'),
    path('dmca', views.dmca, name='dmca'),
    path('privacypolicy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    path('contact', views.contact, name='contact'),
    path('copyright', views.copy, name='copy'),
    path(r'download/', views.download, name='download'),
    path(r"post_upload/", views.post_upload, name='post_upload'),
    path(r'msg/<message>', views.msg, name='msg'),
    path(r'download/msg/<message>', views.msg, name='msg'),
    path('playlist', views.playlist, name='playlist'),
    path(r'playlist_download', views.playlist_download, name='playlist_download'),
    path(r'playlist_upload/', views.playlist_upload, name='playlist_upload'),
    path('mp3', views.mp3, name='mp3'),
    path(r'mp3_download', views.mp3_download, name='mp3_download'),
    path(r'mp3_upload/', views.mp3_upload, name='mp3_upload')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
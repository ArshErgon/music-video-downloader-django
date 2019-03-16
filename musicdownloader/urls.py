"""musicdownloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music.views import music_home,  download_data, trypage, mobile_music_downloader, mobile_music_search, thankyou

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', music_home, name='music'),
    path('download/', download_data, name='download_data'),
    path("try/", trypage, name='try'),
    path("mobile/", mobile_music_search, name="mobile_search"),
    path("result/", mobile_music_downloader, name="mobile_download"),
    path('thank/', thankyou, name='thank'),
]
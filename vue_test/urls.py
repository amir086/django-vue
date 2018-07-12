from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^article/', include('article.urls')),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

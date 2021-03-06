from django.conf.urls import url

from url_mapper.views import HomePage, url_redirect, UrlDetail


urlpatterns = [
    # FIXME: use new url routing
    url(r"^$", HomePage.as_view(), name="home"),
    url(r"^shortened/(?P<shortened>[A-Za-z0-9]+)/$", HomePage.as_view(), name="result"),
    url(r"^(?P<shortened>[A-Za-z0-9]+)/$", url_redirect, name="redirect"),
    url(r"^!(?P<shortened>[A-Za-z0-9]+)/$", UrlDetail.as_view(), name="detail"),
]

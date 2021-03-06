"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainsite.views import homepage, show_stock,show_definition,stock_list,show_useKnown,stock_contact,search,show_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage),
    url(r'^stock/(\w+)$', show_stock),
    url(r'def', show_definition),
    url(r'list',stock_list),
    url(r'useknown', show_useKnown),
    url(r'contact',stock_contact),
    url(r'^search/$',search),
    url(r'error',show_error),
]

from django.conf.urls import url

import closetclient.views 
from django.http import HttpResponse


app_name="closetclient"
urlpatterns = [
    url(r'^$', closetclient.views.index, name='index'),
    url(r'^register$', closetclient.views.register, name='register'),
    url(r'^login$', closetclient.views.login_user, name='login'),
    url(r'^logout$', closetclient.views.user_logout, name='logout'),
    url(r'^categories$', closetclient.views.categories, name='categories'),
    url(r'^view_account$', closetclient.views.view_account, name='view_account'),
    url(r'^add_item$', closetclient.views.add_item, name='add_item'),
]
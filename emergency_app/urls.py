from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    url('^$',views.index, name='index'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url('^login/$',views.user_login, name='login'),
    url('^register/$',views.register,name='register'),
    url('^add/contact/$',views.add_neighbours,name='add-contact'),
    url('^messages/$',views.message_list,name='message-list'),
    url('^messages/new/$',views.send_messsages,name='new_message')

]

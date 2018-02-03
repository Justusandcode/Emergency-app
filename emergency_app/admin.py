from django.contrib import admin
from .models import MyUser,Neighbour,Message

admin.site.register(MyUser)
admin.site.register(Neighbour)
admin.site.register(Message)
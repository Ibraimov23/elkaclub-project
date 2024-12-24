from django.contrib import admin
from .models import User, Post, Topic, City

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(City)
admin.site.register(User)
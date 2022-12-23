from django.contrib import admin
from core.models import FollowersCount, LikePost, Profile,Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
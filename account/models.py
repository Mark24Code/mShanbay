from django.db import models
from django.contrib.auth.models import Group,User

class UserProfile(models.Model):
    user_id = models.CharField(default=0,max_length=100)#用户id
    nickname = models.CharField(max_length=64,null=True)#昵称
    avatar = models.URLField(default='/static/img/default_avatar.jpg')#头像
    created_at = models.DateTimeField(auto_created=True,null=True)#创建日期

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户资料'
        ordering = ['-created_at']

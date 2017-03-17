from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BBS(models.Model):
    title=models.CharField(max_length=64)
    summary=models.CharField(max_length=256,blank=True,null=True)
    content=models.TextField()
    author=models.ForeignKey('BBS_user')
    view_count=models.IntegerField()
    ranking=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=32,unique=True)
    administrator=models.ForeignKey('BBS_user')

class BBS_user(models.Model):

    user=models.OneToOneField(User)
    signature=models.CharField(max_length=128,default='这个家伙很懒，什么都没留下。')
    photo=models.ImageField(upload_to="upload_imgs/",default="upload_imgs/user_1.jpg")

    def __str__(self):
        return self.user.username
#解决中文报错
#alter table junge_bbs_user MODIFY COLUMN photo varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;
from django.db import models

# Create your models here.
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    img = models.FileField(verbose_name="头像", max_length=128, upload_to="admin/",default="admin/管理员头像.svg")

    # 重定义输出方法
    def __str__(self):
        return self.username

class Department(models.Model):
    """部门表"""
    # verbose_name作为注释的作用

    name = models.CharField(verbose_name='部门', max_length=32)
    profile = models.TextField(verbose_name="详细信息")
    img = models.FileField(verbose_name="科室图片", max_length=128, upload_to="depart/")
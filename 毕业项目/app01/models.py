from django.db import models


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    # 重定义输出方法
    def __str__(self):
        return self.username


class Department(models.Model):
    """部门表"""
    # verbose_name作为注释的作用
    name = models.CharField(verbose_name='部门', max_length=32)
    profile = models.TextField(verbose_name="详细信息")
    img = models.FileField(verbose_name="科室图片", max_length=128, upload_to="depart/")

    # 通过重写str方法改变显示
    def __str__(self):
        return self.name


class Doctor(models.Model):
    """医生表"""
    name = models.CharField(verbose_name='姓名', max_length=32)
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    # 当部门被删除的时候，同时删除该医生信息
    depart = models.ForeignKey(verbose_name='所属部门', to='Department', to_field='id', on_delete=models.CASCADE)
    level_choices = ((1, "医师"), (2, "主治医师"), (3, "副主任医师"), (4, "主任医师"))
    level = models.SmallIntegerField(verbose_name='等级', choices=level_choices)
    salary = models.IntegerField(verbose_name='工资')
    day = models.CharField(verbose_name='工作时间', max_length=32)


class Medicine(models.Model):
    """药物表"""
    name = models.CharField(verbose_name='药品名称', max_length=32)
    scale = models.CharField(verbose_name="规格", max_length=32)
    unit_choice = ((0, 'Kg'), (1, '包'), (2, '袋'), (3, '盒'), (4, '瓶'), (5, '支'))
    unit = models.SmallIntegerField(verbose_name='单位', choices=unit_choice)
    price = models.IntegerField(verbose_name='单价')
    category_choice = ((0, '胶囊剂'), (1, '颗粒剂'), (2, '片剂'), (3, '饮片'), (4, '针剂'), (5, '注射剂'), (6, '其他'))
    category = models.SmallIntegerField(verbose_name='类别', choices=category_choice)

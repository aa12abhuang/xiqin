from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootStrapModelForm


class DepartmentModelForm(BootStrapModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"
        # exclude['level'] 排除某些字段

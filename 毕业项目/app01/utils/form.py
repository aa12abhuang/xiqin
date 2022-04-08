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


class DoctorModelForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ["name", "gender", "depart", "level", "salary", "day"]

    # 设置格式

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 遍历设置格式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

from django.shortcuts import render,redirect
from django import forms

# Create your views here.
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from app01 import models

def index(request):
    return render(request,'m-index.html')


class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(render_value=True))

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "m-login.html", {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 使用pop是为了获取数据的同时，清除code，方便下面filter的检验
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "m-login.html", {"form": form})
        # 网站生成随机字符串，写到用户浏览器中，再写入到session中；
        request.session['info'] = {"id": admin_object.id, "name": admin_object.username}
        # 重新设置超时时间，7天免登陆
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/manage/index/")

    return render(request,'m-login.html',{"form": form})

def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/manage/login/")

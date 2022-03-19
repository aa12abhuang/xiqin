import os

from django.shortcuts import render, HttpResponse,redirect
from django import forms
# from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from app01.utils.bootstrap import BootStrapForm, BootStrapModelForm
from app01 import models

def list(request):
    """部门列表"""
    data_dict = {}
    # 没有值则填入默认值""
    search_data = request.GET.get('Search_keshi', "")
    if search_data:
        data_dict["profile__contains"] = search_data

    queryset = models.Department.objects.filter(**data_dict)

    return render(request, 'depart_list.html', {"search_data":search_data,"queryset": queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.Department
        fields = "__all__"


def add(request):
        """"上传文件和数据(modelform)"""
        if request.method == "GET":
            form = UpModelForm()
            return render(request, 'depart_add.html', {"form": form})

        form = UpModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # 自动对文件进行保存，并将字段和上传路径写入到数据库
            form.save()
            return redirect("/depart/list/")
        return render(request, 'depart_add.html', {"form": form})



def delete(request,nid):
    """删除部门"""
    models.Department.objects.filter(id=nid).delete()

    return redirect("/depart/list/")


def edit(request, nid):
    """修改部门"""
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_object": row_object})
    name = request.POST.get("name")
    profile = request.POST.get("profile")
    models.Department.objects.filter(id=nid).update(name=name)
    models.Department.objects.filter(id=nid).update(profile=profile)

    # img_object = request.FILES.get("img")
    # print(img_object)
    # media_path = os.path.join("media/depart/", img_object)
    #
    # f = open(media_path, mode='wb')
    # for chunk in img_object.chunks():
    #     f.write(chunk)
    # f.close()
    # models.Department.objects.filter(id=nid).update(img=media_path)

    return redirect("/depart/list/")


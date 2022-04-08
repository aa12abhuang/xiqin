from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import DoctorModelForm
from django.http import JsonResponse
from openpyxl import load_workbook


def list(request):
    """医生列表"""
    queryset = models.Doctor.objects.all()
    page_object = Pagination(request, queryset, page_size=2)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "doctor_list.html", context)


def add(request):
    """添加医生"""
    if request.method == "GET":
        form = DoctorModelForm()
        return render(request, "doctor_add.html", {"form": form})
    # 获取数据，并进行校验
    form = DoctorModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/doctor/list/')
    return render(request, "doctor_add.html", {"form": form})


def addmore(request):
    return render(request, 'doctor_addmore.html')


def excel(request):
    """批量上传（EXCEl文件),仅适用与xlxs文件"""
    return redirect("/doctor/list/")


def edit(request, nid):
    """编辑医生"""
    row_object = models.Doctor.objects.filter(id=nid).first()

    if request.method == "GET":
        form = DoctorModelForm(instance=row_object)
        return render(request, 'doctor_edit.html', {"form": form})

    form = DoctorModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/doctor/list/')
    return render(request, 'doctor_edit.html', {"form": form})


def delete(request):
    """删除医生"""
    uid = request.GET.get("uid")
    models.Doctor.objects.filter(id=uid).delete()

    return JsonResponse({"status": True})

from django.shortcuts import render

from app.models import Clothes


def index(request):
    """Главная, каталог одежды"""
    clothes = Clothes.objects.all()
    return render(request, "index.html", {"clothes": clothes})


def clothes_info(request, id):
    """Просмотр информации об одежде"""
    clothes = Clothes.objects.get(pk_clothes=id)
    return render(request, "clothes_info.html", {"clothes": clothes})


def admin_index(request):
    """Каталог одежды с кнопками редактирования, удаление, добавления"""
    clothes = Clothes.objects.all()
    return render(request, "admin.html", {"clothes": clothes})

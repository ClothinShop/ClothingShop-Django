from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.models import Clothes
from app.forms import ClothesForm


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


def update_clothes_info(request, id):
    """Обновление информации об одежде"""
    clothes = Clothes.objects.get(pk_clothes=id)

    if request.method == 'POST':
        # Создание формы с заполненными полями
        form = ClothesForm(request.POST, request.FILES)

        if form.is_valid():
            # Изменение полей
            clothes.name = form.cleaned_data["name"]
            clothes.pk_clothes_category = form.cleaned_data["pk_clothes_category"]
            clothes.pk_color = form.cleaned_data["pk_color"]
            clothes.price = form.cleaned_data["price"]
            clothes.sizes = form.cleaned_data["sizes"]
            clothes.description = form.cleaned_data["description"]
            clothes.image_path = form.cleaned_data["image_path"]

            # Сохранение модели
            clothes.save()
            return HttpResponseRedirect('/admin')

    # Создание формы с заполнением полей данными модели
    form = ClothesForm(instance=clothes)
    return render(request, "create_clothes.html", {'form': form, 'id': clothes.pk_clothes})


def create_clothes(request):
    """Добавление одежды"""
    if request.method == 'POST':
        # Создание формы с заполненными полями
        form = ClothesForm(request.POST, request.FILES)

        if form.is_valid():
            # Сохранение модели
            form.save()
            return HttpResponseRedirect('/admin')

    # Создание пустой формы
    form = ClothesForm()
    return render(request, "create_clothes.html", {'form': form})


def delete_clothes(request, id):
    """Удаление одежды"""
    clothes = Clothes.objects.get(pk_clothes=id)
    clothes.delete()
    return HttpResponseRedirect('/admin')

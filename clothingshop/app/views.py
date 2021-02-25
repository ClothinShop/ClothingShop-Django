from django.shortcuts import render

from app.models import Clothes


def index(request):
    # Главная
    clothes = Clothes.objects.all()
    return render(request, "index.html", {"clothes": clothes})

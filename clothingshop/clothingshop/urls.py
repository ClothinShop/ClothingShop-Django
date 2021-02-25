from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    # Каталог
    path('', views.index, name="index"),
    # Страница Админа
    path('admin/', views.admin_index, name="admin"),

    # Просмотр информации об одежеде
    path('product/<int:id>', views.clothes_info, name="clothes_info"),

    # Изменение информации об одежде
    path('product/update/<int:id>', views.update_clothes_info, name="update_clothes_info"),

    # Добавление одежды
    path('product/create/', views.create_clothes, name="create_clothes"),

    # Удаление одежды
    path('product/delete/<int:id>', views.delete_clothes, name="delete_clothes"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

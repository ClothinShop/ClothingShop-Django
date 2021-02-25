from django import forms
from app.models import Clothes, ClothesCategory, Color


class ClothesForm(forms.ModelForm):
    """Форма для редактирования информации об одежде"""
    name = forms.CharField(max_length=255, label="Название")
    name.widget.attrs.update({'class': 'form-control mb-3'})

    pk_clothes_category = forms.ModelChoiceField(queryset=ClothesCategory.objects.all(),
                                                 empty_label=None, label="Категория")
    pk_clothes_category.widget.attrs.update({'class': 'form-control'})

    pk_color = forms.ModelChoiceField(queryset=Color.objects.all(), empty_label=None, label="Цвет")
    pk_color.widget.attrs.update({'class': 'form-control mb-3'})

    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Цена")
    price.widget.attrs.update({'class': 'form-control mb-3'})

    sizes = forms.CharField(max_length=150, label="Размеры")
    sizes.widget.attrs.update({'class': 'form-control mb-3'})

    description = forms.CharField(label="Описание", widget=forms.Textarea, required=False)
    description.widget.attrs.update({'class': 'form-control mb-3'})

    image_path = forms.ImageField(label="Фото", required=False)
    image_path.widget.attrs.update({'class': 'form-control mb-3'})

    class Meta:
        model = Clothes
        fields = ['name', 'pk_clothes_category', 'pk_color', 'price', 'sizes', 'image_path', 'description']

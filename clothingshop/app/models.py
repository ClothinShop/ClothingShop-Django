from django.db import models


class Clothes(models.Model):
    """Одежда"""
    pk_clothes = models.AutoField(db_column='PK_Clothes', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)
    description = models.TextField(db_column='Description', blank=True, null=True)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)
    image_path = models.ImageField(db_column='ImagePath', max_length=255, blank=True, null=True)
    sizes = models.CharField(db_column='Sizes', max_length=150)

    pk_clothes_category = models.ForeignKey('Clothescategory', models.DO_NOTHING,
                                            db_column='PK_ClothesCategory', blank=True, null=True)
    pk_color = models.ForeignKey('Color', models.DO_NOTHING, db_column='PK_Color')

    class Meta:
        db_table = 'Clothes'
        unique_together = (('pk_clothes', 'pk_color'),)


class ClothesCategory(models.Model):
    """Категория"""
    pk_clothes_category = models.AutoField(db_column='PK_ClothesCategory', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    class Meta:
        db_table = 'ClothesCategory'

    def __str__(self):
        return self.name


class Color(models.Model):
    """Цвет"""
    pk_color = models.AutoField(db_column='PK_Color', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    class Meta:
        db_table = 'Color'

    def __str__(self):
        return self.name

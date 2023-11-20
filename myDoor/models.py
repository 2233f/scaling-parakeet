from django.db import models

# Create your models here.
class Merchandise(models.Model):
    merchandise_id = models.AutoField(primary_key=True, verbose_name='商品编号')  # 自增主键
    merchandise_name = models.CharField(max_length=50, verbose_name='商品名称')
    price = models.CharField(max_length=10, verbose_name='商品单价')
    nums = models.CharField(max_length=10, verbose_name='数量')

    class Meta:
        db_table = 'merchandise'
        verbose_name = '商品信息表'
        verbose_name_plural = '商品信息表'
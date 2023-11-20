from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, verbose_name='员工编号')  # 自增主键
    emp_name = models.CharField(max_length=50, verbose_name='员工姓名')
    sex = models.CharField(max_length=10, verbose_name='性别')
    user = models.CharField(max_length=50, verbose_name='账号')
    password = models.CharField(max_length=50, verbose_name='密码')
    create_ts = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')

    class Meta:
        db_table = 'employee'
        verbose_name = '员工信息表'
        verbose_name_plural = '员工信息表'
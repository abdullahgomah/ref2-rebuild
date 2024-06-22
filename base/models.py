from django.db import models

# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=250, verbose_name="اسم اللغة / إطار العمل")


    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'أداة / إطار عمل '
        verbose_name_plural = 'أدوات / أطر عمل'

class DBType(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, verbose_name="اللغة / إطار العمل")
    name = models.CharField(max_length=150, verbose_name="الاسم")

    def __str__(self):
        return str(f"{self.tool} | {self.name}")

    class Meta:
        verbose_name = 'نوع قاعدة بيانات'
        verbose_name_plural = 'أنواع قواعد البيانات'
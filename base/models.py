from django.db import models

# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=250, verbose_name="اسم اللغة / إطار العمل")
    description = models.TextField(verbose_name="نبذه وتفاصيل عن التقنية", null=True, blank=True)
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

class DbFieldType(models.Model):

    db_type = models.ForeignKey(DBType, on_delete=models.CASCADE, related_name='fields_types')
    name = models.CharField(max_length=250, verbose_name="اسم نوع البيانات")
    display_name = models.CharField(verbose_name="الاسم الظاهر", max_length=200)
    cmd = models.TextField() 
    

    def __str__(self):
        return self.name

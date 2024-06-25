from django.db import models
from base.models import * 

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الموقع")
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="اللغة / إطار العمل")
    date_created = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الإنشاء", auto_now_add=True) 

    def __str__(self):
        return self.name 
    
    class Meta: 
        verbose_name = 'موقع'
        verbose_name_plural = "المواقع" 
    

class WebsitePage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, verbose_name="الموقع", related_name='pages')
    name = models.CharField(max_length=250, verbose_name="اسم الصفحة")
    html = models.TextField(verbose_name="html", null=True, blank=True) 
    css = models.TextField(verbose_name="css", null=True, blank=True) 
    js = models.TextField(verbose_name="js", null=True, blank=True) 

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name =  "صفحة موقع"
        verbose_name_plural =  "صفحات المواقع"

class Database(models.Model):
    website = models.ForeignKey(Website, related_name='databases', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="اسم قاعدة البيانات") 
    db_type = models.ForeignKey(DBType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    

    class Meta:
        verbose_name = 'قاعدة بيانات'
        verbose_name_plural = 'قواعد البيانات'


class DbTable(models.Model):
    db = models.ForeignKey(Database, related_name='tables', on_delete=models.CASCADE, verbose_name="قاعدة البيانات")
    name = models.CharField(max_length=250, verbose_name="الاسم")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'جدول'
        verbose_name_plural = 'جداول قواعد البيانات'

class TableField(models.Model):
    db_table = models.ForeignKey(DbTable, related_name='fields', on_delete=models.CASCADE, verbose_name="الجدول")
    name = models.CharField(max_length=200, verbose_name="اسم الحقل")
    data_type = models.ForeignKey("FieldTypes",on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'حقل'
        verbose_name_plural = 'حقول الجداول'


class FieldTypes(models.Model):
    db_type = models.ForeignKey(DBType, verbose_name="نوع قاعدة البيانات", on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="اسم نوع حقل البيانات")
    code = models.TextField(verbose_name="الكود الأساسي") 

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'نوع حقل بيانات'
        verbose_name_plural = 'أنواع حقول البيانات'
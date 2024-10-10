from django.db import models

class ScreenFieldType(models.Model):

    name = models.CharField(max_length=200, unique=True)
    display_name = models.CharField(max_length=200)
    cmd = models.TextField() 

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ScreenFieldType'
        verbose_name_plural = 'ScreenFieldTypes'


class DbType(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'نوع قاعدة بيانات'
        verbose_name_plural = 'أنواع قواعد البيانات'

class Website(models.Model):
    name = models.CharField(max_length=200) 
    url = models.URLField(verbose_name="رابط الموقع")
    db_type = models.ForeignKey(DbType, related_name='websites', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True) 


    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'


class Page(models.Model):
    website = models.ForeignKey('Website', related_name='pages', on_delete=models.CASCADE)
    name = models.CharField(max_length=200 )

    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class ScreenField(models.Model): 
    page = models.ForeignKey('Page', related_name='s_fields', on_delete=models.CASCADE)
    sf_type = models.ForeignKey(ScreenFieldType, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)

    color = models.CharField(verbose_name="اللون", max_length=30, blank=True, null=True)
    width = models.CharField(verbose_name="العرض (بكسل)", max_length=5, blank=True, null=True)
    height = models.CharField(verbose_name="الارتفاع (بكسل)" , max_length=5, blank=True, null=True)
    bg_color = models.CharField(verbose_name="لون الخلفية", max_length=30, blank=True, null=True) 
    bg_url = models.CharField(verbose_name="مسار (رابط ) الخلفية", max_length=255, blank=True, null=True) 
    font_size = models.CharField(max_length=3, verbose_name="حجم الخط (بكسل)", blank=True, null=True)
    font_family = models.CharField(max_length=100, verbose_name="عائلة الخط (اسم الخط)", blank=True, null=True)
    font_weight = models.IntegerField(default=100, verbose_name="وزن الخط (من ١٠٠ إلى ٩٠٠)", blank=True, null=True)
    padding = models.CharField(max_length=5, verbose_name="الهوامش الداخلية (بكسل)", blank=True, null=True)
    margin = models.CharField(max_length=5, verbose_name="الهوامش الخارجية (بكسل)", blank=True, null=True)
    cmd = models.TextField(verbose_name="الأمر البرمجي", null=True, blank=True) 

    def save(self, *args, **kwargs):
        self.cmd = self.sf_type.cmd 
        tag_index = self.cmd.index('>')
        
        self.cmd = self.cmd[:tag_index] + f" id=id{self.id}" + self.cmd[tag_index:]
         
        super(ScreenField, self).save(*args, **kwargs)


    def __str__(self): 
        return self.name 
    

class ExcelTemplate(models.Model):

    file = models.FileField(upload_to='excel/')

    class Meta: 
        verbose_name = 'قالب اكسل'
        verbose_name_plural = "قوالب الاكسل"



class PreBuiltField(models.Model):

    tool = models.ForeignKey("base.Tool", verbose_name="التقنية / الأداة", on_delete=models.SET_NULL, blank=True, null=True, related_name='fields')
    name = models.CharField(verbose_name="اسم الحقل", max_length=200)
    project= models.CharField(verbose_name="المشروع", max_length=200, null=True, blank=True) 
    details = models.TextField(verbose_name="وصف الحقل")
    cmd = models.TextField(verbose_name="سطر الأمر") 

    

    class Meta:
        verbose_name = "حقل "
        verbose_name_plural = "مستودع الحقول"

    def __str__(self):
        return self.name


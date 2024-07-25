from django.db import models

class ScreenFieldType(models.Model):

    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    cmd = models.TextField() 

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ScreenFieldType'
        verbose_name_plural = 'ScreenFieldTypes'


class Website(models.Model):
    name = models.CharField(max_length=200) 
    url = models.URLField(verbose_name="رابط الموقع")
    

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


    def __str__(self): 
        return self.name 
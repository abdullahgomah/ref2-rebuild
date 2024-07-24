from django.db import models

# Create your models here.


class ProjectType(models.Model): 
    name = models.CharField(max_length=200) 

    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name = 'نوع مشروع'
        verbose_name_plural = 'أنواع المشاريع'

class Project(models.Model):
    name = models.CharField(max_length=200)
    p_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        return self.name 
    

    class Meta:
        verbose_name = 'مشروع'
        verbose_name_plural = 'مشاريع'



class FieldType(models.Model): 
    name = models.CharField(max_length=255) 

    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name = 'نوع حقل'
        verbose_name_plural = 'أنواع الحقول'


class Field(models.Model): 
    project =models.ForeignKey(Project, on_delete=models.CASCADE, related_name='fields')  
    name = models.CharField(max_length=250) 
    f_type = models.ForeignKey(FieldType, on_delete=models.CASCADE) 

    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name = 'حقل'
        verbose_name_plural = "حقول"
    

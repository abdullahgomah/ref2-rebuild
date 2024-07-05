# Generated by Django 5.0.6 on 2024-07-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_dbfieldtype_db_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbfieldtype',
            name='display_name',
            field=models.CharField(default='نص', max_length=200, verbose_name='الاسم الظاهر'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dbfieldtype',
            name='name',
            field=models.CharField(max_length=250, verbose_name='اسم نوع البيانات'),
        ),
    ]

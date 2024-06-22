# Generated by Django 5.0.6 on 2024-06-14 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_dbtype_tool'),
        ('website', '0005_alter_website_tool_dbtable_tablefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefield',
            name='db_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='website.dbtable', verbose_name='الجدول'),
        ),
        migrations.AlterField(
            model_name='tablefield',
            name='name',
            field=models.CharField(max_length=200, verbose_name='اسم الحقل'),
        ),
        migrations.CreateModel(
            name='FieldTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم نوع حقل البيانات')),
                ('code', models.TextField(verbose_name='الكود الأساسي')),
                ('db_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dbtype', verbose_name='نوع قاعدة البيانات')),
            ],
            options={
                'verbose_name': 'نوع حقل بيانات',
                'verbose_name_plural': 'أنواع حقول البيانات',
            },
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-24 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'حقل', 'verbose_name_plural': 'حقول'},
        ),
        migrations.AlterModelOptions(
            name='fieldtype',
            options={'verbose_name': 'نوع حقل', 'verbose_name_plural': 'أنواع الحقول'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'مشروع', 'verbose_name_plural': 'مشاريع'},
        ),
        migrations.AlterField(
            model_name='field',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app_v2.project'),
        ),
    ]
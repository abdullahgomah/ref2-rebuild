# Generated by Django 5.0.6 on 2024-06-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_tablefield_data_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء'),
        ),
    ]

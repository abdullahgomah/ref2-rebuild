# Generated by Django 5.0.6 on 2024-06-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_websitepage_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitepage',
            name='css',
            field=models.TextField(blank=True, null=True, verbose_name='css'),
        ),
        migrations.AlterField(
            model_name='websitepage',
            name='html',
            field=models.TextField(blank=True, null=True, verbose_name='html'),
        ),
        migrations.AlterField(
            model_name='websitepage',
            name='js',
            field=models.TextField(blank=True, null=True, verbose_name='js'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_remove_websitepage_css_remove_websitepage_html_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitepage',
            name='css',
            field=models.TextField(blank=True, null=True, verbose_name='css'),
        ),
        migrations.AddField(
            model_name='websitepage',
            name='html',
            field=models.TextField(blank=True, null=True, verbose_name='html'),
        ),
        migrations.AddField(
            model_name='websitepage',
            name='js',
            field=models.TextField(blank=True, null=True, verbose_name='js'),
        ),
    ]

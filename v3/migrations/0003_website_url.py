# Generated by Django 5.0.6 on 2024-07-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0002_screenfieldtype_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='url',
            field=models.URLField(default='https://www.google.com', verbose_name='رابط الموقع'),
            preserve_default=False,
        ),
    ]

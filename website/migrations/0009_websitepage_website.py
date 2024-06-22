# Generated by Django 5.0.6 on 2024-06-22 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_websitepage_code_websitepage_css_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitepage',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='website.website', verbose_name='الموقع'),
        ),
    ]

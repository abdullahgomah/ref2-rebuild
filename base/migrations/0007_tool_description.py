# Generated by Django 5.0.6 on 2024-09-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_dbfieldtype_display_name_alter_dbfieldtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='نبذه وتفاصيل عن التقنية'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-04 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_dbtype_tool'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbFieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cmd', models.TextField()),
                ('db_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dbtype')),
            ],
        ),
    ]

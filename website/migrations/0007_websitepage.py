# Generated by Django 5.0.6 on 2024-06-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_tablefield_db_table_alter_tablefield_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsitePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='اسم الصفحة')),
                ('code', models.TextField(verbose_name='الكود')),
            ],
            options={
                'verbose_name': 'صفحة موقع',
                'verbose_name_plural': 'صفحات المواقع',
            },
        ),
    ]
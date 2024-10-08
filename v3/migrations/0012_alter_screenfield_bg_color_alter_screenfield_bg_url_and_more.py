# Generated by Django 5.0.6 on 2024-08-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0011_screenfield_cmd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenfield',
            name='bg_color',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='لون الخلفية'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='bg_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مسار (رابط ) الخلفية'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='اللون'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='font_family',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عائلة الخط (اسم الخط)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='font_size',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='حجم الخط (بكسل)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='font_weight',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='وزن الخط (من ١٠٠ إلى ٩٠٠)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='height',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='الارتفاع (بكسل)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='margin',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='الهوامش الخارجية (بكسل)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='padding',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='الهوامش الداخلية (بكسل)'),
        ),
        migrations.AlterField(
            model_name='screenfield',
            name='width',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='العرض (بكسل)'),
        ),
    ]

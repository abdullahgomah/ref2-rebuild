# Generated by Django 5.0.6 on 2024-08-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0009_exceltemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenfield',
            name='bg_color',
            field=models.CharField(default='a', max_length=30, verbose_name='لون الخلفية'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='bg_url',
            field=models.CharField(default='', max_length=255, verbose_name='مسار (رابط ) الخلفية'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='color',
            field=models.CharField(default='', max_length=30, verbose_name='اللون'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='font_family',
            field=models.CharField(default='', max_length=100, verbose_name='عائلة الخط (اسم الخط)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='font_size',
            field=models.CharField(default='', max_length=3, verbose_name='حجم الخط (بكسل)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='font_weight',
            field=models.IntegerField(default=100, verbose_name='وزن الخط (من ١٠٠ إلى ٩٠٠)'),
        ),
        migrations.AddField(
            model_name='screenfield',
            name='height',
            field=models.CharField(default='', max_length=5, verbose_name='الارتفاع (بكسل)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='margin',
            field=models.CharField(default='', max_length=5, verbose_name='الهوامش الخارجية (بكسل)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='padding',
            field=models.CharField(default='', max_length=5, verbose_name='الهوامش الداخلية (بكسل)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenfield',
            name='width',
            field=models.CharField(default='', max_length=5, verbose_name='العرض (بكسل)'),
            preserve_default=False,
        ),
    ]

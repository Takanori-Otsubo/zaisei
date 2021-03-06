# Generated by Django 2.2.7 on 2020-01-26 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_event_file2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='file2',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='画像ファイル'),
        ),
        migrations.AlterField(
            model_name='event',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='添付ファイル'),
        ),
    ]

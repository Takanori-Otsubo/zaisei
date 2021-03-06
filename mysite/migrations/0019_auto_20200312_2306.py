# Generated by Django 2.2.7 on 2020-03-12 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0018_auto_20200309_2341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circular',
            options={'ordering': ['-published_at']},
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='join_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='circular',
            name='description',
            field=models.TextField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='circular',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='read_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='join',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

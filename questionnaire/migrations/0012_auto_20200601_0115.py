# Generated by Django 2.2.7 on 2020-05-31 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0011_auto_20200601_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronavirusquestion',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
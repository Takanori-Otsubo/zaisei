# Generated by Django 2.2.7 on 2020-05-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20200524_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronavirusquestion',
            name='deadline',
            field=models.DateField(default='2020-07-01', null=True),
        ),
    ]

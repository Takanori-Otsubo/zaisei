# Generated by Django 2.2.7 on 2020-05-31 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_auto_20200601_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronavirusquestion',
            name='question5_2',
            field=models.IntegerField(choices=[(0, '不満'), (1, 'どちらかと言えば不満'), (2, 'どちらとも言えない'), (3, 'どちらかと言えば満足'), (4, '満足')], null=True, verbose_name='(2)(1)で「はい」の方のみお答えください。テレワークへの評価はどれくらいですか。'),
        ),
        migrations.AlterField(
            model_name='coronavirusquestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

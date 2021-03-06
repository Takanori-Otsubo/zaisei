# Generated by Django 2.2.7 on 2020-01-26 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200123_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='departments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_set', related_query_name='department', to='register.Department', verbose_name='部'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sections',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_set', related_query_name='section', to='register.Section', verbose_name='課'),
        ),
    ]

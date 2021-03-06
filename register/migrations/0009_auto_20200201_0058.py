# Generated by Django 2.2.7 on 2020-01-31 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20200201_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='sections',
        ),
        migrations.RemoveField(
            model_name='user',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sections',
        ),
        migrations.AddField(
            model_name='department',
            name='section',
            field=models.ManyToManyField(null=True, related_name='D_section_set', to='register.Section', verbose_name='課'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='U_department_set', related_query_name='U_department', to='register.Department', verbose_name='部'),
        ),
        migrations.AddField(
            model_name='user',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='U_section_set', related_query_name='U_section', to='register.Section', verbose_name='課'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallproject', '0003_auto_20201004_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='privilege_users',
            field=models.ManyToManyField(related_name='department_privilege', to='smallproject.User'),
        ),
    ]
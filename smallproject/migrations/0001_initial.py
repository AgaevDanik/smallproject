# Generated by Django 3.1.2 on 2020-10-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=400)),
                ('department_image', models.ImageField(upload_to='')),
                ('fees', models.IntegerField(default=0)),
            ],
            options={
                'default_related_name': 'department',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('language_name', models.CharField(max_length=20)),
            ],
            options={
                'default_related_name': 'language',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], default=None, max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('advanced_status', models.BooleanField(default=False)),
                ('departments', models.ManyToManyField(related_name='users', to='smallproject.Department')),
                ('languages', models.ManyToManyField(related_name='users', to='smallproject.Language')),
            ],
            options={
                'default_related_name': 'user',
            },
        ),
    ]

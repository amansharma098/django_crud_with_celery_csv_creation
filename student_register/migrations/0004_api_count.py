# Generated by Django 3.2.4 on 2021-06-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0003_auto_20210622_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_count', models.IntegerField()),
            ],
        ),
    ]

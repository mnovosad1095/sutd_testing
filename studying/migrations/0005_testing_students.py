# Generated by Django 2.1.7 on 2019-02-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('studying', '0004_auto_20190220_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='students',
            field=models.ManyToManyField(to='students.Student'),
        ),
    ]

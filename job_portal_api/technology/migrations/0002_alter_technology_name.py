# Generated by Django 4.1.3 on 2022-11-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]

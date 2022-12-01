# Generated by Django 4.1.3 on 2022-12-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=25)),
                ('github_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('avatar', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]

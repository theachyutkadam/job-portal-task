# Generated by Django 4.1.3 on 2022-11-11 08:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='technology_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='technology.technology'),
            preserve_default=False,
        ),
    ]

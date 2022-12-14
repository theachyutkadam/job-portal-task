# Generated by Django 4.1.3 on 2022-11-15 08:40

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0003_alter_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
                ('detail_overview', models.TextField(max_length=500)),
                ('cover_image', models.ImageField(null=True, upload_to='photos')),
                ('banner_image', models.ImageField(null=True, upload_to='photos')),
                ('is_active', models.BooleanField(default=True)),
                ('learning_mode', models.CharField(max_length=25)),
                ('start_date', models.DateField(max_length=25)),
                ('end_date', models.DateField(max_length=25)),
                ('training_option', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('seats', models.IntegerField(null=True)),
                ('feature', models.CharField(max_length=25)),
                ('requirement', models.CharField(max_length=25)),
                ('eligitbility', models.CharField(max_length=25)),
                ('tools_coverd', models.CharField(max_length=25)),
                ('skill', models.CharField(max_length=25)),
                ('is_free_course', models.BooleanField(blank=True, default=False)),
                ('meta_keywords', models.TextField(max_length=500)),
                ('meta_description', models.TextField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]

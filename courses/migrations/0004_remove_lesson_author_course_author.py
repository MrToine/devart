# Generated by Django 5.0.6 on 2024-06-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson_author_alter_course_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='author',
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default='Anthony Violet', max_length=100),
        ),
    ]

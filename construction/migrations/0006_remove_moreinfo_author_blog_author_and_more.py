# Generated by Django 4.2.1 on 2023-05-14 22:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('construction', '0005_moreinfo_author_alter_blog_date_posted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moreinfo',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
        migrations.AlterField(
            model_name='whatweoffer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 23, 26, 28, 136044)),
        ),
    ]
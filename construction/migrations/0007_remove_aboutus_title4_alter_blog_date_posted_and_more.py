# Generated by Django 4.2.1 on 2023-05-14 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0006_remove_moreinfo_author_blog_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='title4',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 721730)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 706110)),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 706110)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 721730)),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 706110)),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 721730)),
        ),
        migrations.AlterField(
            model_name='whatweoffer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 0, 4, 24, 721730)),
        ),
    ]
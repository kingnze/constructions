# Generated by Django 4.2.1 on 2023-05-14 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0003_banner_alter_blog_date_posted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imggallery', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gallerys',
                'verbose_name_plural': 'Gallerys',
                'db_table': 'gallery',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 740132)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 724511)),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 724511)),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 740132)),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 724511)),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 740132)),
        ),
        migrations.AlterField(
            model_name='whatweoffer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 50, 20, 724511)),
        ),
    ]

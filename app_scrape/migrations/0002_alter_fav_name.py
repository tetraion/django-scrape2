# Generated by Django 3.2.9 on 2021-12-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_scrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='name',
            field=models.TextField(max_length=255, unique=True),
        ),
    ]

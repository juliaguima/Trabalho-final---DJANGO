# Generated by Django 4.2.3 on 2023-07-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0005_model_africa_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_africa',
            name='app',
        ),
        migrations.AddField(
            model_name='model_africa',
            name='foto_2',
            field=models.ImageField(default=11, upload_to='img/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
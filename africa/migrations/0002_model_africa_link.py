# Generated by Django 4.2.3 on 2023-07-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_africa',
            name='link',
            field=models.CharField(default=50, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-26 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0006_remove_model_africa_app_model_africa_foto_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_africa',
            old_name='foto_2',
            new_name='carr',
        ),
    ]

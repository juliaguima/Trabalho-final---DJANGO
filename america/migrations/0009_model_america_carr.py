# Generated by Django 4.2.3 on 2023-07-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0008_comentario_link_url_alter_comentario_eh_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_america',
            name='carr',
            field=models.ImageField(default=1, upload_to='img/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]

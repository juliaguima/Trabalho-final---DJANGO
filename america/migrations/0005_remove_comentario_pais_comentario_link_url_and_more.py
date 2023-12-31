# Generated by Django 4.2.3 on 2023-07-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0004_remove_comentario_link_url_comentario_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='pais',
        ),
        migrations.AddField(
            model_name='comentario',
            name='link_url',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='eh_publicada',
            field=models.BooleanField(default=True),
        ),
    ]

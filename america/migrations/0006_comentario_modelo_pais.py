# Generated by Django 4.2.3 on 2023-07-25 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0005_remove_comentario_pais_comentario_link_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='modelo_pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='america.model_america'),
            preserve_default=False,
        ),
    ]
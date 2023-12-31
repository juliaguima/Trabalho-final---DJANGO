# Generated by Django 4.2.3 on 2023-07-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_africa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Continente', models.CharField(max_length=100)),
                ('País', models.CharField(max_length=100)),
                ('Descricao', models.CharField(max_length=3000)),
                ('OndeFicar', models.CharField(max_length=1800)),
                ('OndeComer', models.CharField(max_length=1800)),
                ('OndeVisitar', models.CharField(max_length=1800)),
                ('foto', models.ImageField(upload_to='img/%Y/%m/%d/')),
                ('ta_publicado', models.BooleanField(default=False)),
            ],
        ),
    ]

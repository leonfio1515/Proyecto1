# Generated by Django 4.0.5 on 2023-05-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasFrec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateField(auto_now_add=True, null=True)),
                ('date_update', models.DateField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('pregunta', models.TextField(max_length=300)),
                ('respuesta', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pregfrec/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Preguntas frecuentes',
                'verbose_name_plural': 'Preguntas frecuentes',
                'ordering': ['date_create'],
            },
        ),
    ]

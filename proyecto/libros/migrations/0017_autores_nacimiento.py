# Generated by Django 5.0.4 on 2024-05-31 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0016_remove_autores_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='autores',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]

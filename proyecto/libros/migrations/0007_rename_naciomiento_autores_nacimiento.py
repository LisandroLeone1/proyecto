# Generated by Django 5.0.4 on 2024-05-28 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_rename_nombre_autores_nombre_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autores',
            old_name='naciomiento',
            new_name='nacimiento',
        ),
    ]
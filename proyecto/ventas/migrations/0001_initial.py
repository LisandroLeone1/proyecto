# Generated by Django 5.0.4 on 2024-05-30 22:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0013_autores_libros_alter_autores_nombre_autor_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='libros.libro')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.vendedor')),
            ],
            options={
                'ordering': ('-fecha_venta',),
            },
        ),
    ]
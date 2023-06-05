# Generated by Django 4.2.1 on 2023-06-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='historiaclinica',
            fields=[
                ('IdOrden', models.AutoField(primary_key=True, serialize=False)),
                ('MedicoVQA', models.CharField(max_length=50)),
                ('MotivoC', models.CharField(max_length=100)),
                ('FechaH', models.DateField()),
                ('Sintomatologia', models.CharField(max_length=100)),
                ('Diagonostico', models.CharField(max_length=200)),
                ('Medicamentov', models.CharField(max_length=50)),
                ('DosisM', models.IntegerField()),
                ('HistorialV', models.DateField()),
                ('MedicamentoA', models.CharField(max_length=50)),
                ('DetalleP', models.CharField(max_length=50)),
                ('AnulaciónO', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='recetarmedicamentos',
            fields=[
                ('IdMedico', models.AutoField(primary_key=True, serialize=False)),
                ('CedulaD', models.IntegerField()),
                ('FechaR', models.DateField()),
                ('NombreMD', models.CharField(max_length=100)),
                ('CedulaV', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=50)),
                ('Contra', models.CharField(max_length=50)),
                ('Tipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registrarmascota',
            fields=[
                ('Nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('CedulaD', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Especie', models.CharField(max_length=50)),
                ('Raza', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('Tamaño', models.IntegerField()),
                ('Peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ventasmedicamentos',
            fields=[
                ('IdFactura', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('IdDueño', models.IntegerField()),
                ('IdMascota', models.IntegerField()),
                ('IdOrden', models.IntegerField()),
                ('NombreP', models.CharField(max_length=100)),
                ('FechaV', models.DateField()),
                ('Valor', models.IntegerField()),
                ('Cantidad', models.IntegerField()),
            ],
        ),
    ]

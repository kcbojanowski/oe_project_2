# Generated by Django 5.0.4 on 2024-04-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealGeneticAlgorithmResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(choices=[('martin_and_gady', 'Martin and Gady'), ('ackleys_function', "Ackley's Function")], max_length=100)),
                ('range_start', models.FloatField()),
                ('range_end', models.FloatField()),
                ('population_size', models.IntegerField()),
                ('chromosome_dimension', models.IntegerField()),
                ('epochs_amount', models.IntegerField()),
                ('elite_amount', models.IntegerField()),
                ('selection_amount', models.IntegerField()),
                ('crossover_rate', models.FloatField()),
                ('mutation_rate', models.FloatField()),
                ('inversion_rate', models.FloatField()),
                ('selection_method', models.CharField(max_length=100)),
                ('crossover_method', models.CharField(max_length=100)),
                ('mutation_method', models.CharField(max_length=100)),
                ('maximization', models.BooleanField(default=False)),
                ('total_time', models.FloatField(blank=True, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_files_real/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

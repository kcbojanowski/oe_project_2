# Generated by Django 5.0.4 on 2024-05-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genetic_algorithm', '0007_rename_chromosome_amount_geneticalgorithmresult_selection_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='geneticalgorithmresult',
            name='tournament_size',
            field=models.IntegerField(null=True, default=20),
            preserve_default=False,
        ),
    ]

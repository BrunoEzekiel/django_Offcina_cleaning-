# Generated by Django 4.1.1 on 2023-03-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_protocole'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
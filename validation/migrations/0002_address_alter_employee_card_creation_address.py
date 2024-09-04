# Generated by Django 5.1.1 on 2024-09-04 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('complement', models.CharField(blank=True, max_length=60, null=True)),
                ('cep', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='employee_card_creation',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='validation.address'),
        ),
    ]

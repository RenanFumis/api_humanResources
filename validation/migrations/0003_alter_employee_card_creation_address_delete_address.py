# Generated by Django 5.1.1 on 2024-09-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_address_alter_employee_card_creation_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_card_creation',
            name='address',
            field=models.JSONField(),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]

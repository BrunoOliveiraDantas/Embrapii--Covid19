# Generated by Django 2.2.14 on 2020-07-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='test_result',
            field=models.CharField(choices=[('PO', 'Positvo'), ('NE', 'Negativo')], max_length=2),
        ),
    ]
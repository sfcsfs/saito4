# Generated by Django 4.1 on 2022-08-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_pension',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
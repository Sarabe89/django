# Generated by Django 4.2.1 on 2023-06-28 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_to_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Number_of_employess',
            field=models.IntegerField(default=1),
        ),
    ]

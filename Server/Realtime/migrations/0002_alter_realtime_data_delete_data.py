# Generated by Django 4.0.6 on 2022-08-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Realtime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtime',
            name='data',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]

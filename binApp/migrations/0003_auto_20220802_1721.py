# Generated by Django 2.2.12 on 2022-08-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binApp', '0002_auto_20220802_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binoperation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.1.15 on 2020-05-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='space',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]

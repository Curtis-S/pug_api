# Generated by Django 2.1.1 on 2018-09-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0002_auto_20180913_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='size',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large'), ('xl', 'extra large')], max_length=2),
        ),
    ]
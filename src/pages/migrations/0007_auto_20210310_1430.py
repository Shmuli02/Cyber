# Generated by Django 3.1.2 on 2021-03-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210310_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bike',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
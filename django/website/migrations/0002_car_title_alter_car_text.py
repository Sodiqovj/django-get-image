# Generated by Django 4.0.4 on 2022-05-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]

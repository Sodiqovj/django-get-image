# Generated by Django 4.0.4 on 2022-05-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_text_car_text1_car_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='text3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

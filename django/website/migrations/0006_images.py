# Generated by Django 4.0.4 on 2022-05-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_car_emblem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]

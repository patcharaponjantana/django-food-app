# Generated by Django 4.2.8 on 2023-12-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_desc', models.CharField(max_length=100)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
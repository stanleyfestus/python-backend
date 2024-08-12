# Generated by Django 4.2.9 on 2024-08-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
            ],
        ),
    ]

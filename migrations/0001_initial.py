# Generated by Django 5.1.2 on 2024-11-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('guesses', models.TextField()),
                ('max_attempts', models.IntegerField(default=6)),
            ],
        ),
    ]
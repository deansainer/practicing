# Generated by Django 4.0.5 on 2022-12-03 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
    ]
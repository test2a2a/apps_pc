# Generated by Django 4.2.7 on 2023-11-20 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=django.utils.timezone.now)),
                ('img', models.ImageField(upload_to='img/')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('info', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]

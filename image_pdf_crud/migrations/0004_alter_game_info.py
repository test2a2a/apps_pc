# Generated by Django 4.2.7 on 2023-11-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_pdf_crud', '0003_game_dec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='info',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]

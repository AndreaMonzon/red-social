# Generated by Django 4.0 on 2022-02-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='perfil1.png', upload_to=''),
        ),
    ]
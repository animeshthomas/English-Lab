# Generated by Django 4.1.7 on 2023-03-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnglishMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EnglishMain.category'),
        ),
    ]

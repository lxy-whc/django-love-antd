# Generated by Django 3.2.4 on 2021-06-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='openid',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='openid'),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailotp',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]

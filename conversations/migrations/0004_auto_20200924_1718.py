# Generated by Django 3.1.1 on 2020-09-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0003_auto_20200924_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]

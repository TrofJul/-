# Generated by Django 2.2.7 on 2019-11-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

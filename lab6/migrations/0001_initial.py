# Generated by Django 2.2.7 on 2019-11-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default=models.CharField(max_length=300), null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

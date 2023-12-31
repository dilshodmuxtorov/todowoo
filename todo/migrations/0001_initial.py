# Generated by Django 5.0 on 2023-12-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=65)),
                ('memo', models.TextField(default='')),
                ('important', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

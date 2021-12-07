# Generated by Django 2.2 on 2021-12-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.CharField(default=100, max_length=100)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

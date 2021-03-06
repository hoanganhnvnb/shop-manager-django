# Generated by Django 2.2 on 2021-12-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('importPrice', models.IntegerField(default=0)),
                ('sellPrice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('companyName', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]

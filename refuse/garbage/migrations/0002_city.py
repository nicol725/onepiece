# Generated by Django 2.2 on 2020-08-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=20)),
                ('good', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.2 on 2020-07-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('participants', models.CharField(max_length=20)),
                ('quote', models.CharField(max_length=100)),
            ],
        ),
    ]

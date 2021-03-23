# Generated by Django 3.1.7 on 2021-03-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('post', models.CharField(blank=True, max_length=50)),
                ('image', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
    ]

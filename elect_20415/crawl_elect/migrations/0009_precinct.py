# Generated by Django 2.1.15 on 2020-04-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl_elect', '0008_delete_precinct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precinct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('sigun', models.CharField(max_length=20)),
                ('dong', models.CharField(max_length=20)),
                ('sgg', models.CharField(max_length=20)),
            ],
        ),
    ]

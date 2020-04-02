# Generated by Django 2.1.15 on 2020-04-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep', models.CharField(max_length=20)),
                ('pic', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('belong', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=100)),
                ('wealth', models.IntegerField()),
                ('military', models.CharField(max_length=50)),
                ('tax_total', models.IntegerField()),
                ('tax_5y', models.IntegerField()),
                ('tax_defalt', models.IntegerField()),
                ('crim_cnt', models.IntegerField()),
                ('candi_cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Precinct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election', models.CharField(max_length=20)),
                ('lawlocation', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.1.15 on 2020-04-04 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawl_elect', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gusigun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gu', models.CharField(max_length=20)),
                ('precint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawl_elect.Precinct')),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='precint',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
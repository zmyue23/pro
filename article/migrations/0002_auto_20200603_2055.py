# Generated by Django 2.0.6 on 2020-06-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='create_date',
            field=models.DateField(blank=True, default='2010-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='status',
            field=models.CharField(blank=True, default=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 2.1.7 on 2019-02-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivaliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalier',
            name='feedback_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
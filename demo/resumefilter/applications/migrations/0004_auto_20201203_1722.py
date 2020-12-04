# Generated by Django 3.1.3 on 2020-12-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20201201_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, upload_to='resume/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='voice',
            field=models.FileField(blank=True, upload_to='audio/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-30 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('github', models.URLField(max_length=254, null=True)),
                ('linkedin', models.URLField(max_length=254, null=True)),
                ('portfolio_site', models.URLField(max_length=254, null=True)),
                ('resume', models.FileField(upload_to='')),
                ('voice', models.FileField(upload_to='')),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='companys.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'unique_together': {('user', 'email')},
            },
        ),
    ]
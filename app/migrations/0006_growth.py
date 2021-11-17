# Generated by Django 3.2.7 on 2021-11-14 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20211113_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('HO', models.IntegerField()),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

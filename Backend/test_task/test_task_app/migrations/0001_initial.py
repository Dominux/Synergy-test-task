# Generated by Django 3.0 on 2019-12-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('position_name', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('fire_date', models.DateField(blank=True, null=True)),
                ('salary', models.PositiveIntegerField()),
                ('fraction', models.PositiveIntegerField()),
                ('base', models.PositiveIntegerField()),
                ('advance', models.PositiveIntegerField()),
                ('by_hours', models.BooleanField()),
            ],
        ),
    ]

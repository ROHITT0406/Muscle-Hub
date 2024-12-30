# Generated by Django 5.1.3 on 2024-12-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plansdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.IntegerField()),
                ('plan', models.CharField(max_length=50)),
                ('sdate', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('payment', models.CharField(max_length=40)),
            ],
        ),
    ]
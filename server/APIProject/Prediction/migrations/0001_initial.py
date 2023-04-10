# Generated by Django 3.2 on 2023-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('sqft', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('bhk', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]

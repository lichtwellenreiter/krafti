# Generated by Django 3.1.4 on 2020-12-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_created=True)),
                ('current_loggedin', models.BigIntegerField()),
                ('current_free', models.BigIntegerField()),
            ],
        ),
    ]

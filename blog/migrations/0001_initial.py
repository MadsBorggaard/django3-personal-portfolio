# Generated by Django 3.1.7 on 2021-04-19 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('createdate', models.DateField(default=datetime.datetime(2021, 4, 19, 17, 48, 14, 810519, tzinfo=utc))),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-04 03:01

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
            ],
            options={
                'verbose_name': 'Participant',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.customuser',),
        ),
    ]

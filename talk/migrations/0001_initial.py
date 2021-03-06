# Generated by Django 3.2.7 on 2021-09-04 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conference', '0001_initial'),
        ('participant', '0001_initial'),
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField()),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conference.conference')),
                ('participants', models.ManyToManyField(related_name='talks_p', to='participant.Participant')),
                ('speakers', models.ManyToManyField(related_name='talks_s', to='speaker.Speaker')),
            ],
        ),
    ]

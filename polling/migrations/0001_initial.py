# Generated by Django 5.1.4 on 2025-01-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(blank=True, max_length=512)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]

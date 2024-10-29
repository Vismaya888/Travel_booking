# Generated by Django 5.1.2 on 2024-10-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('climate', models.CharField(blank=True, max_length=50, null=True)),
                ('best_time_to_visit', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=50, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('popular_attractions', models.TextField(blank=True, help_text='List of popular attractions', null=True)),
                ('recommended_activities', models.TextField(blank=True, help_text='List of recommended activities', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='destinations/')),
            ],
        ),
    ]
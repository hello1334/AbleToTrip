# Generated by Django 5.0.4 on 2024-04-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction_name', models.CharField(max_length=255)),
                ('attraction_sub_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category1', models.CharField(max_length=100)),
                ('category2', models.CharField(blank=True, max_length=100, null=True)),
                ('si', models.CharField(max_length=100)),
                ('gu', models.CharField(max_length=100)),
                ('dong', models.CharField(max_length=100)),
                ('street_number', models.CharField(blank=True, max_length=100, null=True)),
                ('road_name', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('road_name_address', models.CharField(blank=True, max_length=255, null=True)),
                ('lot_number_address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('homepage_url', models.URLField(blank=True, null=True)),
                ('closed_days', models.CharField(blank=True, max_length=255, null=True)),
                ('operation_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('is_free_parking', models.BooleanField(default=False)),
                ('is_paid_parking', models.BooleanField(default=False)),
                ('is_entrance_fee', models.BooleanField(default=False)),
                ('is_disabled_restroom', models.BooleanField(default=False)),
                ('is_disabled_parking', models.BooleanField(default=False)),
                ('is_large_parking', models.BooleanField(default=False)),
                ('is_audio_guide', models.BooleanField(default=False)),
                ('attraction_image', models.BinaryField(blank=True, default=None, null=True)),
            ],
        ),
    ]

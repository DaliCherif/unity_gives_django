# Generated by Django 5.0.6 on 2024-05-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('donation_name', models.CharField(max_length=50)),
                ('donation_type', models.CharField(max_length=50)),
                ('donation_amount', models.CharField(max_length=50)),
                ('donation_reference', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('donor_name', models.CharField(max_length=50)),
                ('donor_address', models.CharField(max_length=50)),
                ('donor_number', models.CharField(max_length=50)),
            ],
        ),
    ]
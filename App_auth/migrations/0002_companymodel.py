# Generated by Django 4.1.4 on 2023-01-09 16:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Must add +880', regex='^\\+?(88)01[3-9][0-9]{8}$')])),
                ('primary_phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_number', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycinfo',
            name='long_text',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

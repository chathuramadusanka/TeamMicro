# Generated by Django 3.1.7 on 2021-04-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0003_auto_20210410_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc_infotemp',
            name='id_type_temp',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

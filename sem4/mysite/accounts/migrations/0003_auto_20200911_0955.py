# Generated by Django 3.1 on 2020-09-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200911_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

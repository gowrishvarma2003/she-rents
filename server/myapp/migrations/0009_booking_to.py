# Generated by Django 5.0.4 on 2024-04-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='to',
            field=models.CharField(default='9494768855', max_length=200),
            preserve_default=False,
        ),
    ]

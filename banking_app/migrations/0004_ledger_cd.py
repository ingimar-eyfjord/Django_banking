# Generated by Django 3.2.7 on 2021-10-09 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banking_app', '0003_account_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='cd',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=255),
            preserve_default=False,
        ),
    ]

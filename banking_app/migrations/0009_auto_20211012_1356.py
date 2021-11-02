# Generated by Django 3.2.7 on 2021-10-12 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banking_app', '0008_rename_account_owner_ledger_account_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='credit',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ledger',
            name='debit',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]

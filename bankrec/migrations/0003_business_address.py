# Generated by Django 5.1.3 on 2024-11-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bankrec", "0002_rename_payment_method_transactionentry_transaction_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

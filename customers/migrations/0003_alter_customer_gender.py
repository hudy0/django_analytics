# Generated by Django 5.1rc1 on 2024-08-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0002_alter_customer_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="M", max_length=1
            ),
        ),
    ]

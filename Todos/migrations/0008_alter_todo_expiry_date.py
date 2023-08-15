# Generated by Django 4.2.3 on 2023-07-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Todos", "0007_alter_todo_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="expiry_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Expiry Date(mm/dd/yyyy)"
            ),
        ),
    ]

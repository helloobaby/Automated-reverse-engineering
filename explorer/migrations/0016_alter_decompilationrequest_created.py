# Generated by Django 3.2.19 on 2023-11-20 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0015_alter_decompilationrequest_index_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decompilationrequest',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

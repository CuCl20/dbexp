# Generated by Django 4.1.3 on 2022-11-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_state_delete_service_remove_client_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default=222, max_length=20),
            preserve_default=False,
        ),
    ]

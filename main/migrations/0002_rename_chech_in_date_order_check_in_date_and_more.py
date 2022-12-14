# Generated by Django 4.1.3 on 2022-11-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='chech_in_date',
            new_name='check_in_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='chech_out_date',
            new_name='check_out_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pey_method',
            new_name='pay_method',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(max_length=4),
        ),
    ]

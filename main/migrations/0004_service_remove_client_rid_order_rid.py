# Generated by Django 4.1.3 on 2022-11-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_client_rid_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=11)),
                ('time', models.DateTimeField()),
                ('place', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='rid',
        ),
        migrations.AddField(
            model_name='order',
            name='rid',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
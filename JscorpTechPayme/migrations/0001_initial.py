# Generated by Django 5.0.3 on 2024-03-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=255)),
                ('request_id', models.IntegerField()),
                ('order_key', models.CharField(max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('processing', 'processing'), ('success', 'success'), ('failed', 'failed'), ('canceled', 'canceled')], default='processing', max_length=55)),
                ('perform_datetime', models.CharField(max_length=255, null=True)),
                ('cancel_datetime', models.CharField(max_length=255, null=True)),
                ('created_datetime', models.CharField(max_length=255, null=True)),
                ('reason', models.IntegerField(null=True)),
            ],
        ),
    ]

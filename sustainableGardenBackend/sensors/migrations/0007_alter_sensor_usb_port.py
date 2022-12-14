# Generated by Django 3.2 on 2022-04-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0006_alter_sensor_usb_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='usb_port',
            field=models.CharField(choices=[('/dev/ttyACM0', 'Arduino MEGA'), ('/dev/ttyUSB1', 'USB1'), ('/dev/ttyUSB2', 'USB2'), ('/dev/ttyUSB3', 'USB3')], default='com3', max_length=50),
        ),
    ]

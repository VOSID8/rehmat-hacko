# Generated by Django 4.2 on 2023-04-16 08:17

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='doctor_id',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='upload/doctor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='refugee_card',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.validationimage'),
        ),
        migrations.AlterField(
            model_name='validationimage',
            name='file',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=user.models.id_upload_to),
        ),
    ]
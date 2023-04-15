# Generated by Django 4.1.7 on 2023-04-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0004_rename_token_scheduledslot_token1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledslot',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='scheduledslot',
            name='token1',
        ),
        migrations.RemoveField(
            model_name='scheduledslot',
            name='token2',
        ),
        migrations.RemoveField(
            model_name='scheduledslot',
            name='uid1',
        ),
        migrations.RemoveField(
            model_name='scheduledslot',
            name='uid2',
        ),
        migrations.AddField(
            model_name='scheduledslot',
            name='slug',
            field=models.CharField(default=None, max_length=600, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='scheduledslot',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]

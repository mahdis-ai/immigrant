# Generated by Django 4.0.1 on 2022-01-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='visa_type',
            field=models.CharField(choices=[('work', 'work'), ('study', 'study')], default='study', max_length=100),
        ),
    ]
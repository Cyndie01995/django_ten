# Generated by Django 5.0.2 on 2024-03-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DB', 'DRAFT'), ('PB', 'PUBLISHED')], default='DB', max_length=2),
        ),
    ]

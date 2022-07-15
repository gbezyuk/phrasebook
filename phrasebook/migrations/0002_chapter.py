# Generated by Django 4.0.3 on 2022-07-15 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrasebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'chapter',
                'verbose_name_plural': 'chapters',
            },
        ),
    ]

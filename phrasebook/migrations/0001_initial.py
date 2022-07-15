# Generated by Django 4.0.3 on 2022-07-15 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('original', models.CharField(max_length=255, verbose_name='original')),
                ('transcription', models.CharField(max_length=255, verbose_name='transcription')),
                ('translation', models.CharField(max_length=255, verbose_name='translation')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phrases', to='phrasebook.language', verbose_name='language')),
            ],
            options={
                'verbose_name': 'phrase',
                'verbose_name_plural': 'phrases',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PhraseAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='uploads/phrase_audios/', verbose_name='file')),
                ('phrase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='audios', to='phrasebook.phrase', verbose_name='phrase')),
            ],
            options={
                'verbose_name': 'phrase audio',
                'verbose_name_plural': 'phrase audios',
            },
        ),
        migrations.AddField(
            model_name='phrase',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='phrases', to='phrasebook.tag', verbose_name='tags'),
        ),
        migrations.AlterUniqueTogether(
            name='phrase',
            unique_together={('language', 'original')},
        ),
    ]
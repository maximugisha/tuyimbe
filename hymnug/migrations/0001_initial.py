# Generated by Django 3.2.4 on 2021-06-23 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255, null=True)),
                ('image_url', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
                ('expired', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hymn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HymnNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=3)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HymnFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField()),
                ('lyrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_lyrics', to='hymnug.hymn')),
            ],
        ),
        migrations.AddField(
            model_name='hymn',
            name='hymn_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hymn_number', to='hymnug.hymnnumber'),
        ),
        migrations.AddField(
            model_name='hymn',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hymn_language', to='hymnug.language'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-15 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'Statsy Event',
                'verbose_name_plural': 'Statsy Events',
            },
        ),
        migrations.CreateModel(
            name='StatsyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'Statsy Group',
                'verbose_name_plural': 'Statsy Groups',
            },
        ),
        migrations.CreateModel(
            name='StatsyObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at')),
                ('float_value', models.FloatField(blank=True, null=True, verbose_name='float value')),
                ('text_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='text value')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='duration')),
                ('extra', jsonfield.fields.JSONField(blank=True, max_length=1024, null=True, verbose_name='extra')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statsy_object_list', to='statsy.StatsyEvent', verbose_name='event')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statsy_object_list', to='statsy.StatsyGroup', verbose_name='group')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statsy_object_list', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Statsy Object',
                'verbose_name_plural': 'Statsy Objects',
                'ordering': ('-created_at',),
                'permissions': (('stats_view', 'Can view stats'),),
            },
        ),
        migrations.AlterIndexTogether(
            name='statsyobject',
            index_together={('content_type', 'object_id', 'user')},
        ),
    ]

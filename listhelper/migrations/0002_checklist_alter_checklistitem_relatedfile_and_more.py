# Generated by Django 5.0.6 on 2024-06-05 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listhelper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='relatedFile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listhelper.file'),
        ),
        migrations.CreateModel(
            name='ChecklistHasChacklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listhelper.checklist')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listhelper.checklistitem')),
            ],
        ),
    ]
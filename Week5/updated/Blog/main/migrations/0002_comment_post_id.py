# Generated by Django 2.1.2 on 2018-10-05 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Post'),
        ),
    ]
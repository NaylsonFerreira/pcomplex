# Generated by Django 3.1.4 on 2021-03-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology_app', '0003_auto_20210307_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
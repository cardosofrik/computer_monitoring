# Generated by Django 2.0 on 2020-02-15 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dispositivo', '0008_auto_20200215_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabelaend',
            name='ario',
        ),
        migrations.AddField(
            model_name='tabelaend',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.fields.related.OneToOneField, related_name='tabelaend', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
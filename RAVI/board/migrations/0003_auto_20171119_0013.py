# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_item_kompletcolour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='position',
        ),
        migrations.RemoveField(
            model_name='item',
            name='positionColour',
        ),
    ]

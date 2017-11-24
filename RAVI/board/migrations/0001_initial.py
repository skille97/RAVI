# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idColour', models.TextField()),
                ('name', models.TextField(verbose_name='Projekt')),
                ('nameColour', models.TextField()),
                ('position', models.IntegerField(unique=True)),
                ('positionColour', models.TextField()),
                ('komplet', models.BooleanField(verbose_name='Komplet', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VærdiModel',
            fields=[
                ('item', models.OneToOneField(serialize=False, to='board.Item', primary_key=True)),
                ('colour', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Antal',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Kommentar',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Komponenter',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Levering',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Montage',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='PCB',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
        migrations.CreateModel(
            name='Stencil',
            fields=[
                ('værdimodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='board.VærdiModel', primary_key=True)),
                ('value', models.TextField()),
            ],
            bases=('board.værdimodel',),
        ),
    ]

# Generated by Django 3.2.25 on 2024-04-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('name', models.TextField()),
                ('wuli', models.TextField()),
                ('zhili', models.TextField()),
                ('texing1', models.TextField()),
                ('texing2', models.TextField()),
                ('texing3', models.TextField()),
                ('bishaji', models.TextField()),
                ('yili', models.TextField()),
                ('xiangxing', models.TextField()),
                ('zhongzu', models.TextField()),
                ('gender', models.TextField()),
                ('img', models.TextField()),
                ('figure', models.TextField()),
                ('desc', models.TextField()),
                ('text_all', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

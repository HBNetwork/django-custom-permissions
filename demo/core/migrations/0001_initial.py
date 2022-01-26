# Generated by Django 4.0.1 on 2022-01-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'permissions': (('core.blog.rename', 'Can rename title.'), ('core.blog.publish', 'Can publish post.')),
            },
        ),
    ]

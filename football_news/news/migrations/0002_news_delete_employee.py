# Generated by Django 4.1.4 on 2023-03-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
                ('paragraph3', models.TextField()),
                ('photo', models.ImageField(blank=True, default=None, upload_to='news_photos/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
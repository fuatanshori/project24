# Generated by Django 4.2.4 on 2023-09-07 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('news_title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=55)),
                ('news_description', models.TextField()),
                ('news_image', models.ImageField(blank=True, default='static/assets/img/defaultnewskotak.png', null=True, upload_to='media/news')),
                ('is_publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'permissions': [('can_publish_news', 'Can Publish News'), ('can_preview_news', 'Can Preview News')],
            },
        ),
    ]
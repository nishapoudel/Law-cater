# Generated by Django 4.0.6 on 2022-11-23 15:15

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='post/')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawcaterapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lawcaterapp.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

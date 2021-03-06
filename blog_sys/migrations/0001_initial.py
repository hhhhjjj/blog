# Generated by Django 2.2 on 2019-06-11 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_password', models.CharField(max_length=100)),
                ('author_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('blog_read_number', models.PositiveIntegerField()),
                ('blog_publish_time', models.DateField(auto_now=True)),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_sys.Author')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'theme',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('comment_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_sys.Blog')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_sys.Author')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_sys.Comment')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog_sys.Theme'),
        ),
    ]

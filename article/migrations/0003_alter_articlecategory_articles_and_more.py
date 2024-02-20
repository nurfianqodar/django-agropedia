# Generated by Django 5.0.2 on 2024-02-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_options_alter_article_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='category', related_query_name='categories', to='article.article'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-02 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('material_type', models.CharField(choices=[('theory', 'Theoretical Material'), ('practice', 'Practical')], default='theory', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_materials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

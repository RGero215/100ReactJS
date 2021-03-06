# Generated by Django 2.2.3 on 2019-09-15 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourPomodoro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.BooleanField(default=False)),
                ('player_four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four_pomodoro_player_four', to=settings.AUTH_USER_MODEL)),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('player_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four_pomodoro_player_three', to=settings.AUTH_USER_MODEL)),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four_pomodoro_player_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

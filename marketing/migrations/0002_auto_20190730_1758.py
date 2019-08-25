# Generated by Django 2.2.3 on 2019-07-30 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='player',
        ),
        migrations.AddField(
            model_name='groups',
            name='player_eight',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_eight', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_eleven',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_elven', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_fifteen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_fifteen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_five',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_five', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_four',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_four', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_fourteen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_fourteen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_nine',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_nine', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_one',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_seven',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_seven', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_six',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_six', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_sixteen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_sixteen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_ten',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_ten', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_thirteen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_thirteen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_three',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_three', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_twelve',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_twelve', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='player_two',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to=settings.AUTH_USER_MODEL),
        ),
    ]

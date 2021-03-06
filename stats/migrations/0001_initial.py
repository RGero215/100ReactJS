# Generated by Django 2.2.3 on 2019-08-27 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='account.png', upload_to='one_player_pics')),
                ('firstAtBats', models.IntegerField(default=0)),
                ('firstAvg', models.IntegerField(default=0)),
                ('firstDoubles', models.IntegerField(default=0)),
                ('firstHits', models.IntegerField(default=0)),
                ('firstHomeRuns', models.IntegerField(default=0)),
                ('firstLob', models.IntegerField(default=0)),
                ('firstPoints', models.IntegerField(default=0)),
                ('firstRbi', models.IntegerField(default=0)),
                ('firstRuns', models.IntegerField(default=0)),
                ('firstSingles', models.IntegerField(default=0)),
                ('firstSlg', models.IntegerField(default=0)),
                ('firstTriples', models.IntegerField(default=0)),
                ('firstResult', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('firstHome', models.IntegerField(default=0)),
                ('firstAway', models.IntegerField(default=0)),
                ('firstRisk', models.IntegerField(default=0)),
                ('firstSafe', models.IntegerField(default=0)),
                ('firstGrandSlam', models.IntegerField(default=0)),
                ('firstOff', models.IntegerField(default=0)),
                ('firstStop', models.IntegerField(default=0)),
                ('firstLevel', models.CharField(blank=True, default='Rookie', max_length=20, null=True)),
                ('firstFinal', models.BooleanField(default=False)),
                ('secondAtBats', models.IntegerField(default=0)),
                ('secondAvg', models.IntegerField(default=0)),
                ('secondDoubles', models.IntegerField(default=0)),
                ('secondHits', models.IntegerField(default=0)),
                ('secondHomeRuns', models.IntegerField(default=0)),
                ('secondLob', models.IntegerField(default=0)),
                ('secondPoints', models.IntegerField(default=0)),
                ('secondRbi', models.IntegerField(default=0)),
                ('secondRuns', models.IntegerField(default=0)),
                ('secondSingles', models.IntegerField(default=0)),
                ('secondSlg', models.IntegerField(default=0)),
                ('secondTriples', models.IntegerField(default=0)),
                ('secondResult', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('secondHome', models.IntegerField(default=0)),
                ('secondAway', models.IntegerField(default=0)),
                ('secondRisk', models.IntegerField(default=0)),
                ('secondSafe', models.IntegerField(default=0)),
                ('secondGrandSlam', models.IntegerField(default=0)),
                ('secondOff', models.IntegerField(default=0)),
                ('secondStop', models.IntegerField(default=0)),
                ('secondLevel', models.CharField(blank=True, default='Rookie', max_length=20, null=True)),
                ('secondFinal', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Four')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atBats', models.IntegerField(default=0)),
                ('avg', models.IntegerField(default=0)),
                ('doubles', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('homeRuns', models.IntegerField(default=0)),
                ('lob', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('rbi', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('singles', models.IntegerField(default=0)),
                ('slg', models.IntegerField(default=0)),
                ('triples', models.IntegerField(default=0)),
                ('result', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('winnings', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('home', models.IntegerField(default=0)),
                ('away', models.IntegerField(default=0)),
                ('image', models.ImageField(default='100React.png', upload_to='stats_pics')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('opponent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to=settings.AUTH_USER_MODEL)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnePLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='account.png', upload_to='one_player_pics')),
                ('atBats', models.IntegerField(default=0)),
                ('avg', models.IntegerField(default=0)),
                ('doubles', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('homeRuns', models.IntegerField(default=0)),
                ('lob', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('rbi', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('singles', models.IntegerField(default=0)),
                ('slg', models.IntegerField(default=0)),
                ('triples', models.IntegerField(default=0)),
                ('result', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('home', models.IntegerField(default=0)),
                ('away', models.IntegerField(default=0)),
                ('risk', models.IntegerField(default=0)),
                ('safe', models.IntegerField(default=0)),
                ('grandSlam', models.IntegerField(default=0)),
                ('off', models.IntegerField(default=0)),
                ('stop', models.IntegerField(default=0)),
                ('level', models.CharField(blank=True, default='Rookie', max_length=20, null=True)),
                ('final', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

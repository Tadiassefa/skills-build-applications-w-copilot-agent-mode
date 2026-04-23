from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='pass', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='pass', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='pass', first_name='Bruce', last_name='Banner', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='pass', first_name='Clark', last_name='Kent', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='bruce@dc.com', password='pass', first_name='Bruce', last_name='Wayne', team=dc)

        # Workouts
        run = Workout.objects.create(name='Running', description='Run fast!')
        lift = Workout.objects.create(name='Weight Lifting', description='Lift heavy!')
        fly = Workout.objects.create(name='Flying', description='Fly high!')

        # Activities
        Activity.objects.create(user=tony, workout=run, duration=30, calories=300)
        Activity.objects.create(user=steve, workout=run, duration=45, calories=400)
        Activity.objects.create(user=bruce, workout=lift, duration=60, calories=500)
        Activity.objects.create(user=clark, workout=fly, duration=50, calories=600)
        Activity.objects.create(user=bruce_dc, workout=lift, duration=40, calories=350)

        # Leaderboard
        Leaderboard.objects.create(user=tony, points=1000)
        Leaderboard.objects.create(user=steve, points=900)
        Leaderboard.objects.create(user=bruce, points=800)
        Leaderboard.objects.create(user=clark, points=950)
        Leaderboard.objects.create(user=bruce_dc, points=850)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups')
        self.assertEqual(workout.name, 'Pushups')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', email='activity@example.com', password='testpass')
        workout = Workout.objects.create(name='Situps', description='Do situps')
        activity = Activity.objects.create(user=user, workout=workout, duration=30, calories=100)
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.calories, 100)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='leaderuser', email='leader@example.com', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, points=50)
        self.assertEqual(leaderboard.points, 50)

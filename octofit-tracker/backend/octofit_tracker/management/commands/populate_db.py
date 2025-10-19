from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard'),
            Workout.objects.create(name='Agility Boost', description='Agility and flexibility exercises', difficulty='Medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-10-19')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2025-10-18')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2025-10-17')
        Activity.objects.create(user=users[3], type='Boxing', duration=40, calories=400, date='2025-10-16')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750, rank=1)
        Leaderboard.objects.create(team=dc, points=700, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

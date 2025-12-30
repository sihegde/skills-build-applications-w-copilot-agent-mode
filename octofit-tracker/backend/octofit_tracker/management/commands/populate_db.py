from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users (Super Heroes)
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': marvel},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = app_models.User.objects.create(name=u['name'], email=u['email'], team=u['team'])
            user_objs.append(user)

        # Create Activities
        activities = [
            {'user': user_objs[0], 'type': 'Run', 'duration': 30},
            {'user': user_objs[1], 'type': 'Swim', 'duration': 45},
            {'user': user_objs[2], 'type': 'Bike', 'duration': 60},
            {'user': user_objs[3], 'type': 'Run', 'duration': 25},
            {'user': user_objs[4], 'type': 'Swim', 'duration': 50},
            {'user': user_objs[5], 'type': 'Bike', 'duration': 70},
        ]
        for a in activities:
            app_models.Activity.objects.create(user=a['user'], type=a['type'], duration=a['duration'])

        # Create Workouts
        workouts = [
            {'name': 'Morning Cardio', 'description': 'Cardio session for all'},
            {'name': 'Strength Training', 'description': 'Strength and resistance'},
        ]
        for w in workouts:
            app_models.Workout.objects.create(name=w['name'], description=w['description'])

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=300)
        app_models.Leaderboard.objects.create(team=dc, points=280)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

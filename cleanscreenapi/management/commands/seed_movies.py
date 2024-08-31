# from django.core.management.base import BaseCommand
# from cleanscreenapi.models import Movie

# class Command(BaseCommand):
#     help = 'Seed the database with movies'

#     def handle(self, *args, **kwargs):
#         movies = [
#             {
#                 'title': 'The Exorcist',
#                 'year': 1973,
#                 'rating': 'R',
#                 'genre': 'Horror',
#                 'user_rating_total': 4,
#                 'user_rating_count': 1000
#             },
#             {
#                 'title': 'Babylon',
#                 'year': 2022,
#                 'rating': 'R',
#                 'genre': 'Drama',
#                 'user_rating_total': 3.8,
#                 'user_rating_count': 800
#             },
#             {
#                 'title': 'It',
#                 'year': 2017,
#                 'rating': 'R',
#                 'genre': 'Horror',
#                 'user_rating_total': 4.1,
#                 'user_rating_count': 1200
#             }
#         ]

#         for movie_data in movies:
#             Movie.objects.create(**movie_data)

#         self.stdout.write(self.style.SUCCESS('Successfully seeded the database with movies'))
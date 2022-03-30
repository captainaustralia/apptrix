import os
from django.core.mail import send_mail
from math import radians, asin, sqrt, sin, cos


def get_file_path(obj, fname):
    return os.path.join(
        'user_avatar',
        obj.email,
        fname
    )


def send_messages(user_1, user_2):
    send_mail(
        'Hello',
        f'Вы понравились {user_1.name}! Почта участника: {user_1.email}',
        'apptrixtesttask1@gmail.com',
        [user_2],
        fail_silently=False
    )
    send_mail(
        'Hello',
        f'Вы понравились {user_2.name}! Почта участника: {user_2.email}',
        'apptrixtesttask1@gmail.com',
        [user_1],
        fail_silently=False
    )


def get_distance_between_users(long_point, lat_point, long_us, lat_us):
    lon1, lat1, lon2, lat2 = map(radians, [long_point, lat_point, long_us, lat_us])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    distance = 2 * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
    km = 6371 * distance
    return round(km, 3)

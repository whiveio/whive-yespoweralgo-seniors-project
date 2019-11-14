import datetime
import geocoder
import os
from collections import namedtuple

# Offsets of different timezones with respect to GMT
EARLIEST_AFRICAN_TIMEZONE = -1
LATEST_AFRICAN_TIMEZONE = 4
EARLIEST_ASIAN_TIMEZONE = 5
EARLIEST_EUROPEAN_TIMEZONE = 0

# The top left and bottom right coordinates of rectangle in 2D grid of world
# map that determines different regions.
RegionCoordinates = namedtuple(
        'RegionCoordinates',
        ('top_left_x', 'top_left_y', 'bottom_right_x', 'bottom_right_y'))

CARRIBEAN_REGION = RegionCoordinates(-90, 30, -45, 15)
SOUTH_AMERICAN_REGION = RegionCoordinates(-90, 15, -30, -60)
AFRICAN_REGION = RegionCoordinates(-20, 30, 50, -45)
ASIAN_REGION = RegionCoordinates(50, 30, 90, -30)

# Percentage rewards associated with each region.
CARRIBEAN_REGION_REWARD = 20
SOUTH_AMERICAN_REGION_REWARD = 15
AFRICAN_REGION_REWARD = 45
ASIAN_REGION_REWARD = 15
OTHER_REGION_REWARD = 5

# This constant value is used to compute machine coordinates percentage reward.
MAX_COORDINATES_SUM = 120


def get_processor_reward():
    """Returns reward percentage based on machine processor."""
    processor = os.uname().machine
    if processor.startswith('x86_64'):
        return 35
    elif processor.startswith('arm'):
        return 55
    else:
        return 10


def get_timezone():
    """Returns number of hours machine's timezone is behind utc's timezone."""
    time_difference = datetime.datetime.now() - datetime.datetime.utcnow()
    return time_difference.total_seconds() / 3600


def get_timezone_reward():
    """Returns reward percentage based on machine's timezone."""
    timezone = get_timezone()
    if EARLIEST_AFRICAN_TIMEZONE < timezone <= EARLIEST_EUROPEAN_TIMEZONE:
        return 35
    elif EARLIEST_EUROPEAN_TIMEZONE < timezone <= LATEST_AFRICAN_TIMEZONE:
        return 45
    elif LATEST_AFRICAN_TIMEZONE < timezone <= EARLIEST_ASIAN_TIMEZONE:
        return 15
    else:
        return 5


def get_machine_coordinates_reward(latitude, longitude):
    """Returns percentage reward based on the input coordinates."""
    if (CARRIBEAN_REGION.top_left_x <= longitude <
            CARRIBEAN_REGION.bottom_right_x and
            CARRIBEAN_REGION.bottom_right_y <= latitude <
            CARRIBEAN_REGION.top_left_y):
        return CARRIBEAN_REGION_REWARD
    elif (SOUTH_AMERICAN_REGION.top_left_x <= longitude <
            SOUTH_AMERICAN_REGION.bottom_right_x and
            SOUTH_AMERICAN_REGION.bottom_right_y <= latitude <
            SOUTH_AMERICAN_REGION.top_left_y):
        return SOUTH_AMERICAN_REGION_REWARD
    elif (AFRICAN_REGION.top_left_x <= longitude <
            AFRICAN_REGION.bottom_right_x and
            AFRICAN_REGION.bottom_right_y <= latitude <
            AFRICAN_REGION.top_left_y):
        return AFRICAN_REGION_REWARD
    elif (ASIAN_REGION.top_left_x <= longitude <
            ASIAN_REGION.bottom_right_x and
            ASIAN_REGION.bottom_right_y <= latitude <
            ASIAN_REGION.top_left_y):
        return ASIAN_REGION_REWARD
    else:
        return OTHER_REGION_REWARD
   

def get_multi_tier_reward():
    """
    Returns percentange reward based on device's architecture and location or
    timezone. Computes coordinates reward if machines' coordinates are
    accessable. Else, timezone reward is computed based on devices' timezone.
    """
    device_coordinates = geocoder.ip('me')
    location_reward = get_machine_coordinates_reward(
            device_coordinates.latlng) if device_coordinates else get_timezone_reward()
    processor_reward = get_processor_reward()
    total_percentage_reward = (location_reward + processor_reward) / 2
    return total_percentage_reward

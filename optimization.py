import datetime
import geocoder
import os

# Offsets of different timezones with respect to GMT
EARLIEST_AFRICAN_TIMEZONE = -1
LATEST_AFRICAN_TIMEZONE = 4
EARLIEST_ASIAN_TIMEZONE = 5
EARLIEST_EUROPEAN_TIMEZONE = 0

# Coorindate points that form optimal rectangle in the globe.
# Device with (latitude, longitude) that is inside this rectangle gets maximum
# machine coordinates reward.
LEFT_BOUND = -90
RIGHT_BOUND = 90
TOP_BOUND = 30
BOTTOM_BOUND = -30

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

def get_machine_coordinates_reward(device_coordinates):
    """Returns percentage reward based on the input coordinates."""
    latitude, longitude = device_coordinates
    if LEFT_BOUND <= latitude <= RIGHT_BOUND and BOTTOM_BOUND <= longitude <= TOP_BOUND:
        return (abs(latitude) + abs(longitude)) / MAX_COORDINATES_SUM
    else:
        return 5

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

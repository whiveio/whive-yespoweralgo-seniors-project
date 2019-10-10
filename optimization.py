import datetime
import os

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
    time_difference = datetime.datetime.utcnow() - datetime.datetime.now()
    return time_difference.total_seconds() / 3600

def get_timezone_reward():
    """Returns reward percentage based on machine's timezone."""
    timezone = get_timezone()
    # TODO(henxing): Implement this after understanding the pseudocode.
    pass

def get_machine_coordinates_reward(coordinates):
    # TODO(henxing): Implement this after understanding the design doc.
    pass

def get_device_coordinates():
    """Returns latitude and longitude of device as a tuple."""
    # TODO(henxing): Implement this after finding a way to find device's
    #                coordinate.
    pass

def get_multi_tier_reward():
    # TODO(henxing): Implement after understanding design doc.
    device_coordinates = get_device_coordinates()
    location_reward = get_machine_coordinates_reward(
            device_coordinates) if device_coordinates else get_timezone_reward()
    processor_reward = get_processor_reward()
    total_percentage_reward = (location_reward + processor_reward) / 2
    return total_percentage_reward



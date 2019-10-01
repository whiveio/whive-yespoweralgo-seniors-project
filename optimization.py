import sys
from time import gmtime, strftime

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'linux' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]

def get_timezone():
    return strftime("%z", gmtime())

def reward():
    platform = get_platform()
    timezone = int(get_timezone())
    reward = 0
    if platform == 'ARM':
        reward = 0.4
    elif platform == "Windows":
        reward = 0.1
    elif platform == 'OS X':
        reward = 0.2
    elif platform == 'Linux':
        reward = 0.3
    else:
        reward = 0
    
    if timezone >= 0 and timezone <= 400:
      reward *= .80
    elif timezone >= 500 and timezone <= 1200:
      reward *= .40
    else:
      reward *= .30
    return reward
reward()
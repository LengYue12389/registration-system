from config import Config


def set_dnf_time(time):
    if time == Config.DNF_TIME:
        time = 'DNF '
    return time

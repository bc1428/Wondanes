from datetime import datetime


def stopwatch(function, request=None):
    """
    Measures the time of a process
    command : stopwatch([function], [Desired time information])
    0: start
    1: stop
    100: all
    None: stop - start (microsecond)
    """

    def inner():
        start = datetime.now()
        function()
        stop = datetime.now()
        timedown = (stop - start)
        if request == 0:
            return start
        elif request == 1:
            return stop
        elif request == 100:
            return [start, stop, timedown.seconds]
        else:
            return timedown.seconds

    return inner


def convert_time(microsecond, unit):
    """
    0: seconder
    #1: minute
    :param unit: Unit time [Second/Minute]
    :param microsecond: A unit time
    """
    try:
        print(microsecond)
        seconder = microsecond / 1000000
        # minute = seconder/60 # Will be added soon
        units = [seconder]  # Add minute
        return units[unit]
    except TypeError:
        pass

def active_time(start_time):
    difference_time = datetime.now() - start_time
    return difference_time

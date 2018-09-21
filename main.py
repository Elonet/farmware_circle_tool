# -*- coding: utf-8 -*-

import os
from utils import log
from farmbot import FarmBot
from geometry import Circle


def get_parameters():
    """
    Get parameters

    :return: Farmware parameters (radius, speed, steps)
    :rtype: tuple
    """
    try:
        ra = int(os.environ.get('circle_tool_radius', '100'))
        sp = int(os.environ.get('circle_tool_speed', '800'))
        st = int(os.environ.get('circle_tool_steps', '8'))
    except ValueError:
        raise Exception('Wrong parameters format')

    if ra < 1:
        raise Exception('Radius ( > 1 )')
    if sp < 1:
        raise Exception('Speed ( > 1 )')
    if st < 2:
        raise Exception('Steps ( > 2 )')

    return ra, sp, st


if __name__ == '__main__':
    log('Started', 'debug')

    try:
        radius, speed, steps = get_parameters()

        log('Radius : {0}, Speed: {1}, Steps: {2}'.format(radius, speed, steps), 'debug')
        farmbot = FarmBot()

        current_position = farmbot.position
        log('Current position: ' + str(current_position), 'debug')

        path = Circle(current_position, radius, steps).points
        log('Movements to do: {0}'.format(len(path)), 'debug')

        for position in path:
            farmbot.move(position, speed)

    except Exception as ex:
        log('Error --> {0}'.format(ex), 'error')

    log('Finished', 'debug')

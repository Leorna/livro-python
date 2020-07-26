import enum


class Color(enum.Enum):
    GREEN = 1
    RED = 2
    YELLOW = 3


# ns = north/south
# es = east/west
market_2nd = { 'ns': Color.GREEN, 'ew': Color.RED }
mission_16th = { 'ns': Color.RED, 'ew': Color.GREEN }


def switch_lights(stoplight: dict):
    for key in stoplight.keys():
        if stoplight[key] == Color.GREEN:
            stoplight[key] = Color.YELLOW
        elif stoplight[key] == Color.YELLOW:
            stoplight[key] = Color.RED
        elif stoplight[key] == Color.RED:
            stoplight[key] = Color.GREEN

    assert Color.RED in stoplight.values(), f'Neither light is red {stoplight}'


switch_lights(market_2nd)
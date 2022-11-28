''' Synthetic signal module '''
from random import gauss

# Sensor MIN and MAX ranges
SENSOR_MAX = 100
SENSOR_MIN = -100

MU = 0
MAIN_VARIANCE = 24.5
MINOR_VARIANCE = 0.6


class Signal:
    ''' Main class for a synthetic signal (a Gaussian process) '''
    def __init__(self) -> None:
        self._value = gauss(MU, MAIN_VARIANCE)

    @property
    def value(self) -> float:
        delta = gauss(MU, MINOR_VARIANCE)
        current_value = self._value + delta
        if current_value < SENSOR_MIN:
            self._value += (-1.0 if delta < 0 else 1.0) * delta
            current_value += 4 * delta
        elif current_value > SENSOR_MAX:
            self._value -= (-1.0 if delta < 0 else 1.0) * delta
            current_value += 4 * delta
        else:
            self._value = current_value
        return current_value



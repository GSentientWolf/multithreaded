from .base_sensor import BaseSensor
from utils.network import Network


class ThermalSensor(BaseSensor):
    ''' Thermal sensor '''
    def __init__(self, *, name: str, network: Network, interval:int = 5) -> None:
        super().__init__(name=name, network=network)
        self.sensortype = 'thermal'
        self.interval = interval


class VibrationSensor(BaseSensor):
    ''' Vibration sensor '''
    def __init__(self, *, name: str, network: Network, interval:int = 5) -> None:
        super().__init__(name=name, network=network)
        self.sensortype = 'vibration'
        self.interval = interval\


class MagneticSensor(BaseSensor):
    ''' Magnetic Sensor '''
    def __init__(self, *, name: str, network: Network, interval: int = 5) -> None:
        super().__init__(name=name, network=network)
        self.sensortype = 'magnetic'
        self.interval = interval

 
class HumititySensor(BaseSensor):

    def __init__(self, *, name: str, network: Network, inteval: int = 5) -> None:
        super().__init__(name=name, network=network)
        self.sensortype = 'humitity'
        self.interval = interval



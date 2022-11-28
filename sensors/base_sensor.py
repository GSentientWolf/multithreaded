import datetime
import threading
import json
from typing import Union, Callable
from utils.network import Network
from .signal import Signal


class BaseSensor(threading.Thread):
    """ Base class for any sensor type"""

    def __init__(self, *, name: str, network: Network):
        """ Initialize with required named parameters """
        self.name = name
        self.network = network
        self.signal = Signal()
        self.send_readout_fn = None

    @property
    def readout(self) -> str:
        """
        This property provides the sensor message's main body
        :return: Updated json readout for the sensor.
        """
        out = self.__dict__
        out.pop('signal')
        out.update({'value': str(self.signal.value)})
        out.update({'posix_timestamp': datetime.now().timestamp()})
        out = {'readout': out}
        return json.dumps(out)

    @property
    def send_readout_fn(self) -> callable:
        """ Returns the stored logger callback function """
        return self._readout_callback_fn

    @send_readout_fn.setter
    def send_readout_fn(self, fn: Union[Callable[[...], None] | None]) -> None:
        """ Stores de callback function when the sensor is registered """
        self._readout_callback_fn = fn

    def send_readout(self) -> None:
        """
        Sends sensor readout to the logger module via the provided callback
        function
        """
        self.send_readout_fn(self.readout)




""" Internal message structure """

import json
from typing import Protocol
from enum import Enum


class MessageEnum(str, Enum):
    pass


class SensorMessageEnum(MessageEnum):
    SENSOR_ONLINE = 'SENSOR_ONLINE'
    SENSOR_OFFLINE = 'SENSOR_OFFLINE'
    SENSOR_READOUT = 'SENSOR_READOUT'
    SENSOR_OUT_OF_RANGE = 'SENSOR_OUT_OF_RANGE'


class Message(Protocol):
    msg_type: MessageEnum
    msg_content: str


class SensorMessage:
    def __init__(self, message: str):
        self.msg_type = SensorMessageEnum
        self.msg_content = message

    @property
    def message(self):
        return json.dumps(self.__dict__)


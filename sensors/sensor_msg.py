from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from .sensor import BaseSensor


class Sensor(BaseModel):
    name: str
    timestamp: datetime
    value: str


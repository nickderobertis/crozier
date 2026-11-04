

import typing

from .fixed_sensor import FixedSensor
from .mobile_sensor import MobileSensor

CreateSensorsRequest = typing.Union[FixedSensor, MobileSensor]

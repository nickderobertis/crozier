

import typing

from .fixed_sensor import FixedSensor
from .mobile_sensor import MobileSensor

CreateFleetsRequestSensorsItem = typing.Union[FixedSensor, MobileSensor]

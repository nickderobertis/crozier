

import typing

from .manual_trigger import ManualTrigger
from .tide_trigger import TideTrigger
from .wind_trigger import WindTrigger

Trigger = typing.Union[ManualTrigger, TideTrigger, WindTrigger]

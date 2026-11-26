

import typing

from .manual_trigger import ManualTrigger
from .surge_alarm import SurgeAlarm

Alarm = typing.Union[ManualTrigger, SurgeAlarm]

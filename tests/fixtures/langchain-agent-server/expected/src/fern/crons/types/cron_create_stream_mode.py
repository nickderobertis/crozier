

import typing

from .cron_create_stream_mode_one import CronCreateStreamModeOne
from .cron_create_stream_mode_zero_item import CronCreateStreamModeZeroItem

CronCreateStreamMode = typing.Union[typing.List[CronCreateStreamModeZeroItem], CronCreateStreamModeOne]

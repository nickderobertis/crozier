

import typing

from .cron_expression import CronExpression
from .relative_delta import RelativeDelta
from .time_delta import TimeDelta

ScheduleInterval = typing.Union[TimeDelta, RelativeDelta, typing.Optional[CronExpression]]



import typing

from .lifetime_days import LifetimeDays
from .lifetime_hours import LifetimeHours
from .lifetime_minutes import LifetimeMinutes
from .lifetime_seconds import LifetimeSeconds

Lifetime = typing.Union[LifetimeSeconds, LifetimeMinutes, LifetimeHours, LifetimeDays]

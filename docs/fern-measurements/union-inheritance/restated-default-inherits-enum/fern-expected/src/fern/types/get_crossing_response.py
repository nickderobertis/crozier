

import typing

from .crossing_boarding_notice import CrossingBoardingNotice
from .crossing_delayed_notice import CrossingDelayedNotice
from .crossing_sailed_notice import CrossingSailedNotice

GetCrossingResponse = typing.Union[CrossingDelayedNotice, CrossingSailedNotice, CrossingBoardingNotice]

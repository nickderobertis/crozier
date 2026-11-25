

import typing

from .event_vessel_arrived import EventVesselArrived
from .event_vessel_departed import EventVesselDeparted

Event = typing.Union[EventVesselArrived, EventVesselDeparted]

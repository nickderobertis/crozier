

import typing

from .vent_alert_levels import VentAlertLevels
from .vent_alert_one import VentAlertOne

VentAlert = typing.Union[VentAlertLevels, VentAlertOne]

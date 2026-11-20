

import typing

from .vent_alert import VentAlert
from .vent_closed_alert import VentClosedAlert

GetAlertResponse = typing.Union[VentAlert, VentClosedAlert]

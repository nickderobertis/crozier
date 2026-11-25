

import typing

from .session_shutter_one import SessionShutterOne
from .session_shutter_zero import SessionShutterZero

SessionShutter = typing.Union[SessionShutterZero, SessionShutterOne]

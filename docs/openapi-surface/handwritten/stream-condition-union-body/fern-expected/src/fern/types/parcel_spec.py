

import typing

from .crate import Crate
from .tracking_code import TrackingCode

ParcelSpec = typing.Union[TrackingCode, Crate]

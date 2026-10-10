

import typing

from .crate import Crate
from .tracking_code import TrackingCode

EstimateRequest = typing.Union[TrackingCode, Crate]

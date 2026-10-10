

import typing

from .crate import Crate
from .tracking_code import TrackingCode

EstimateStreamRequest = typing.Union[TrackingCode, Crate]

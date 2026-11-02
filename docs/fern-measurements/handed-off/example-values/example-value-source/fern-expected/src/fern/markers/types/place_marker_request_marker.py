

import typing

from ...types.buoy_marker import BuoyMarker
from ...types.light_marker import LightMarker

PlaceMarkerRequestMarker = typing.Union[BuoyMarker, LightMarker]



import typing

from .depth_centimetres import DepthCentimetres
from .gauge_reading import GaugeReading

WaterLevel = typing.Union[DepthCentimetres, GaugeReading]

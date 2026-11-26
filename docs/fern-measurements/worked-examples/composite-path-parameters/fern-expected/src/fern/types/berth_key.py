

import typing

from .buoy_key import BuoyKey
from .slip_key import SlipKey

BerthKey = typing.Union[SlipKey, BuoyKey]

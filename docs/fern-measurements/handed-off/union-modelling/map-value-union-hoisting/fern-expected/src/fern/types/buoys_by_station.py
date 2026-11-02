

import typing

from .buoy import Buoy

BuoysByStation = typing.Dict[str, typing.Optional[Buoy]]
"""
Buoys keyed by station, each possibly absent.
"""

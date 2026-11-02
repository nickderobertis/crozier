

import typing

from .soundings_by_station_value import SoundingsByStationValue

SoundingsByStation = typing.Dict[str, SoundingsByStationValue]
"""
Soundings keyed by station, as an inline union.
"""

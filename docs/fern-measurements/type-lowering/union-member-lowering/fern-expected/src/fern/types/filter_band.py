

import typing

from .filter_band_one import FilterBandOne
from .filter_band_zero import FilterBandZero

FilterBand = typing.Union[FilterBandZero, FilterBandOne]

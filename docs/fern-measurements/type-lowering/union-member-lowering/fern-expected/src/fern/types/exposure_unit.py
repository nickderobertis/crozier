

import typing

from .exposure_unit_one import ExposureUnitOne
from .exposure_unit_zero import ExposureUnitZero

ExposureUnit = typing.Union[ExposureUnitZero, ExposureUnitOne]



import typing

from .exposure_mode_one import ExposureModeOne
from .exposure_mode_zero import ExposureModeZero

ExposureMode = typing.Union[ExposureModeZero, ExposureModeOne]

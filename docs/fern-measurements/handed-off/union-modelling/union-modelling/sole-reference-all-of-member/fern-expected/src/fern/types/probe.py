

import typing

from .anemometer import Anemometer
from .hygrometer import Hygrometer
from .thermometer import Thermometer

Probe = typing.Union[Thermometer, Hygrometer, Anemometer]

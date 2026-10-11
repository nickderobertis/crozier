

import typing

from .analog import Analog
from .digital import Digital

Signal = typing.Union[Analog, Digital]

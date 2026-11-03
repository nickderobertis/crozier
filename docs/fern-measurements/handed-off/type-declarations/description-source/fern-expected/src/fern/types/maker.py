

import typing

from .apprentice import Apprentice
from .glassblower import Glassblower

Maker = typing.Union[Glassblower, Apprentice]

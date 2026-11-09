

import typing

from .aerotow import Aerotow
from .winch import Winch

Launch = typing.Union[Winch, Aerotow]

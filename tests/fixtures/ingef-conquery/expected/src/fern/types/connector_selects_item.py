

import typing

from .select import Select
from .universal_select import UniversalSelect

ConnectorSelectsItem = typing.Union[Select, UniversalSelect]

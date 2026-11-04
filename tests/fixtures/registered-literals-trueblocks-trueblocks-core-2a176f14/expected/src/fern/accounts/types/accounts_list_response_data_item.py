

import typing

from ...types.appearance import Appearance
from ...types.bounds import Bounds
from ...types.monitor import Monitor

AccountsListResponseDataItem = typing.Union[Appearance, Bounds, Monitor]

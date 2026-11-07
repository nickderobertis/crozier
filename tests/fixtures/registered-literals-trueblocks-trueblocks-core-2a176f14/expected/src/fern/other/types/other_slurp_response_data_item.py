

import typing

from ...types.appearance import Appearance
from ...types.function import Function
from ...types.monitor import Monitor
from ...types.parameter import Parameter
from ...types.slurp import Slurp

OtherSlurpResponseDataItem = typing.Union[Appearance, Function, Monitor, Parameter, Slurp]

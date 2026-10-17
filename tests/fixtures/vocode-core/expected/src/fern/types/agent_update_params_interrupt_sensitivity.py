

import typing

from .interrupt_sensitivity import InterruptSensitivity
from .undefined import Undefined

AgentUpdateParamsInterruptSensitivity = typing.Union[InterruptSensitivity, Undefined]

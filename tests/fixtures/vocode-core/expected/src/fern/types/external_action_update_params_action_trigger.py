

import typing

from .function_call_action_trigger import FunctionCallActionTrigger
from .undefined import Undefined

ExternalActionUpdateParamsActionTrigger = typing.Union[FunctionCallActionTrigger, Undefined]

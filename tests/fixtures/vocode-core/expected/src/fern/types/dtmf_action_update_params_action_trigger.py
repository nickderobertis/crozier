

import typing

from .function_call_action_trigger import FunctionCallActionTrigger
from .undefined import Undefined

DtmfActionUpdateParamsActionTrigger = typing.Union[FunctionCallActionTrigger, Undefined]

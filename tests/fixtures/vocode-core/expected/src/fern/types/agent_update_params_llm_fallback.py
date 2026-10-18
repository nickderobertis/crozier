

import typing

from .internal_llm_fallback import InternalLlmFallback
from .undefined import Undefined

AgentUpdateParamsLlmFallback = typing.Union[InternalLlmFallback, Undefined]

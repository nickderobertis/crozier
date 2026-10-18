

import typing

from .prompt_update_params import PromptUpdateParams
from .undefined import Undefined

AgentUpdateParamsPrompt = typing.Union[str, PromptUpdateParams, Undefined]



import typing

from .agent_update_params_voice_one import AgentUpdateParamsVoiceOne
from .undefined import Undefined

AgentUpdateParamsVoice = typing.Union[str, AgentUpdateParamsVoiceOne, Undefined]



import typing

from .agent_update_params_deepgram_keywords_zero_value import AgentUpdateParamsDeepgramKeywordsZeroValue
from .undefined import Undefined

AgentUpdateParamsDeepgramKeywords = typing.Union[
    typing.Dict[str, AgentUpdateParamsDeepgramKeywordsZeroValue], Undefined
]

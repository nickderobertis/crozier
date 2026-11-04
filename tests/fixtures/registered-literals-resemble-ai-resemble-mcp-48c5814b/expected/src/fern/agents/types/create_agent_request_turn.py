

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_agent_request_turn_mode import CreateAgentRequestTurnMode


class CreateAgentRequestTurn(UniversalBaseModel):
    turn_timeout: typing.Optional[int] = None
    silence_end_call_timeout: typing.Optional[int] = None
    mode: typing.Optional[CreateAgentRequestTurnMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

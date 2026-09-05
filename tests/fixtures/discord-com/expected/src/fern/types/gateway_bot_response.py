

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gateway_bot_session_start_limit_response import GatewayBotSessionStartLimitResponse


class GatewayBotResponse(UniversalBaseModel):
    url: str
    session_start_limit: GatewayBotSessionStartLimitResponse
    shards: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

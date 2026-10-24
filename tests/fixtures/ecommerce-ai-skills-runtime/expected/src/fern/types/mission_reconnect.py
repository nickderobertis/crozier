

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mission_reconnect_reason import MissionReconnectReason


class MissionReconnect(UniversalBaseModel):
    reason: MissionReconnectReason
    retry_after_seconds: int
    cursor: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

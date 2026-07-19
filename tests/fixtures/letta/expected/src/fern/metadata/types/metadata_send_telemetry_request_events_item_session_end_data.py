

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSendTelemetryRequestEventsItemSessionEndData(UniversalBaseModel):
    session_id: str
    agent_id: typing.Optional[str] = None
    duration: float
    message_count: float
    tool_call_count: float
    exit_reason: typing.Optional[str] = None
    total_api_ms: typing.Optional[float] = None
    total_wall_ms: typing.Optional[float] = None
    prompt_tokens: typing.Optional[float] = None
    completion_tokens: typing.Optional[float] = None
    total_tokens: typing.Optional[float] = None
    cached_tokens: typing.Optional[float] = None
    reasoning_tokens: typing.Optional[float] = None
    step_count: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

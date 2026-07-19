

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSendTelemetryRequestEventsItemToolUsageData(UniversalBaseModel):
    session_id: str
    agent_id: typing.Optional[str] = None
    tool_name: str
    success: bool
    duration: float
    response_length: typing.Optional[float] = None
    error_type: typing.Optional[str] = None
    stderr: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

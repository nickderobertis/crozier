

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSendTelemetryRequestEventsItemErrorData(UniversalBaseModel):
    session_id: str
    agent_id: typing.Optional[str] = None
    run_id: typing.Optional[str] = None
    error_type: str
    error_message: str
    context: typing.Optional[str] = None
    http_status: typing.Optional[float] = None
    model_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

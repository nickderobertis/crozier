

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSendTelemetryRequestEventsItemSessionStartData(UniversalBaseModel):
    session_id: str
    agent_id: typing.Optional[str] = None
    startup_command: str
    version: typing.Optional[str] = None
    platform: typing.Optional[str] = None
    node_version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

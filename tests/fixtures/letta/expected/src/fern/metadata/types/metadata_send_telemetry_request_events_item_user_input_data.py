

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSendTelemetryRequestEventsItemUserInputData(UniversalBaseModel):
    session_id: str
    agent_id: typing.Optional[str] = None
    input_length: float
    is_command: bool
    command_name: typing.Optional[str] = None
    message_type: str
    model_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

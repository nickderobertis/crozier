

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .ingestion_event_seven_type import IngestionEventSevenType
from .sdk_log_event import SdkLogEvent


class IngestionEventSeven(SdkLogEvent):
    type: IngestionEventSevenType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amf_event_trigger import AmfEventTrigger


class AmfEventMode(UniversalBaseModel):
    trigger: AmfEventTrigger
    max_reports: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxReports"), pydantic.Field(alias="maxReports")
    ] = None
    expiry: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MessageAttempetLast(UniversalBaseModel):
    id: str
    response_status_code: typing_extensions.Annotated[
        int, FieldMetadata(alias="responseStatusCode"), pydantic.Field(alias="responseStatusCode")
    ]
    timestamp: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

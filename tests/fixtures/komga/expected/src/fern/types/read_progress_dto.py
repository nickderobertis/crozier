

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReadProgressDto(UniversalBaseModel):
    completed: bool
    created: dt.datetime
    device_id: typing_extensions.Annotated[str, FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")]
    device_name: typing_extensions.Annotated[str, FieldMetadata(alias="deviceName"), pydantic.Field(alias="deviceName")]
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    page: int
    read_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="readDate"), pydantic.Field(alias="readDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

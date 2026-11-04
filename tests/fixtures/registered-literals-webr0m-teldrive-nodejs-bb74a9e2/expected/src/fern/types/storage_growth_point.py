

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageGrowthPoint(UniversalBaseModel):
    day: dt.date
    added_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="addedBytes"), pydantic.Field(alias="addedBytes")]
    logical_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="logicalBytes"), pydantic.Field(alias="logicalBytes")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReviewDelegationWeek(UniversalBaseModel):
    week_start: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="weekStart"), pydantic.Field(alias="weekStart")
    ]
    replied: int
    accepted_unedited: typing_extensions.Annotated[
        int, FieldMetadata(alias="acceptedUnedited"), pydantic.Field(alias="acceptedUnedited")
    ]
    edited: int
    unknown: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

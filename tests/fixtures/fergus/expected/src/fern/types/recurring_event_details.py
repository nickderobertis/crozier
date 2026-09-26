

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RecurringEventDetails(UniversalBaseModel):
    start_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ]
    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    r_rule: typing_extensions.Annotated[str, FieldMetadata(alias="rRule"), pydantic.Field(alias="rRule")]
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

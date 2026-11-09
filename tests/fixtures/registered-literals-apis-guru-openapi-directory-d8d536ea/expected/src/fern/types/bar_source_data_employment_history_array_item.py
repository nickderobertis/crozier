

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataEmploymentHistoryArrayItem(UniversalBaseModel):
    employer: typing.Optional[str] = None
    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

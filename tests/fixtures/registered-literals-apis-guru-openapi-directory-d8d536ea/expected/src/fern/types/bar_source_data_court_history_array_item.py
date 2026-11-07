

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataCourtHistoryArrayItem(UniversalBaseModel):
    action: typing.Optional[str] = None
    action_comments: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actionComments"), pydantic.Field(alias="actionComments")
    ] = None
    reinstated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="reinstatedDate"), pydantic.Field(alias="reinstatedDate")
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

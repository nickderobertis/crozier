

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AxisSectionTreeless(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    url: typing.Optional[str] = None
    code: str
    multilingual_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="multilingualName"), pydantic.Field(alias="multilingualName")
    ]
    description: typing.Optional[str] = None
    owner_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")
    ] = None
    start_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startOn"), pydantic.Field(alias="startOn")
    ] = None
    end_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endOn"), pydantic.Field(alias="endOn")
    ] = None
    active: typing.Optional[bool] = None
    axis_id: typing_extensions.Annotated[int, FieldMetadata(alias="axisId"), pydantic.Field(alias="axisId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SliceLs(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="_id"), pydantic.Field(alias="_id")] = (
        None
    )
    name: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="created at"), pydantic.Field(alias="created at")
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

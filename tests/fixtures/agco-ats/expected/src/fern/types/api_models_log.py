

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsLog(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ID"), pydantic.Field(alias="ID")] = None
    message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Message"), pydantic.Field(alias="Message")
    ] = None
    time_stamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="TimeStamp"), pydantic.Field(alias="TimeStamp")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

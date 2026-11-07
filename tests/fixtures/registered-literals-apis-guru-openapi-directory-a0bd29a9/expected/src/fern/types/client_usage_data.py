

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClientUsageData(UniversalBaseModel):
    active_minutes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeMinutes"), pydantic.Field(alias="activeMinutes")
    ] = None
    last_activity: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastActivity"), pydantic.Field(alias="lastActivity")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

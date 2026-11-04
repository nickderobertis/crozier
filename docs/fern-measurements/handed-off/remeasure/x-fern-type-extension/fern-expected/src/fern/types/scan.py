

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Scan(UniversalBaseModel):
    captured_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="capturedAt"), pydantic.Field(alias="capturedAt")
    ] = None
    queued_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="queuedAt"), pydantic.Field(alias="queuedAt")
    ] = None
    active: typing.Optional[typing.Literal[True]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TelemetryData(UniversalBaseModel):
    level: typing.Optional[str] = None
    message: typing.Optional[str] = None
    optional_values: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[str]]],
        FieldMetadata(alias="optionalValues"),
        pydantic.Field(alias="optionalValues"),
    ] = None
    time: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
